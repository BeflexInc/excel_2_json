from __future__ import print_function
from openpyxl import load_workbook

import json
import os.path
import io

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']


def downloadTextResourceFromDrive():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            # q="name = 'beflex_app_text_resource'",
            q="name = 'jump_rope_textresource'",
            fields="nextPageToken, files(id, name)",
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
        ).execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            textResourceFileId = item['id']
            print(u'{0} ({1})'.format(item['name'], item['id']))

        request = service.files().export_media(fileId=textResourceFileId,
                                               mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        fh = io.FileIO('../assets/resource.xlsx', 'w+')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def convertExcelToJson():
    projectResourcePath = ''
    filesize = os.path.getsize('../assets/flutter_project_resource_path.txt')
    if (filesize == 0):
        path = input('flutter project i18n path :')
        i18nLocation = open('../assets/flutter_project_resource_path.txt', 'w')
        i18nLocation.write(path)
        i18nLocation.close()
        projectResourcePath = path
    else:
        projectResourcePath = open('../assets/flutter_project_resource_path.txt', 'r').read()

    loadedExcel = load_workbook('../assets/resource.xlsx', data_only=True)

    # 활성화된 시트 가져오기
    loadedSheet = loadedExcel.active

    # 새 언어 추가될때마다 주석 풀어주면 됨
    targetLangCode = {'B': loadedSheet['B1'].value, 'C': loadedSheet['C1'].value,
                      # 'D': loadedSheet['D1'].value,
                      # 'E': loadedSheet['E1'].value, 'F': loadedSheet['F1'].value, 'G': loadedSheet['G1'].value,
                      }
    langCodeKey = list(targetLangCode.keys())
    keyList = []
    valueList = []
    json_dict = {}

    # 첫번째 column이 key 값.
    # Key 값 배열 만들기
    for row in loadedSheet['A']:
        keyList.append(row.value)

    for element in langCodeKey:
        # Value 배열 만들기
        for row in loadedSheet[element]:
            if type(row.value) == float:
                valueList.append("{}".format(int(row.value)))
            else:
                valueList.append("{}".format(row.value))
        json_dict = dict(zip(keyList, valueList))
        valueList = []
        # 첫 번째 row 의 언어 코드 row 지우기
        del (json_dict[keyList[0]])
        # 변환
        with open(projectResourcePath + '/' + str(targetLangCode[element]) + '.json', 'w', encoding='UTF-8') as outfile:
            json.dump(json_dict, outfile, ensure_ascii=False, indent='\t')
            print('Done with ' + str(targetLangCode[element]))


def main():
    downloadTextResourceFromDrive()
    convertExcelToJson()


if __name__ == '__main__':
    main()
