import json
from openpyxl import load_workbook

excelFile = input("Excel File name : ")

loadedExcel = load_workbook('../assets/' + excelFile, data_only=True)

loadedSheet = loadedExcel['Sheet1']

targetLangCode = {'B': 'en-US', 'C': 'zh-CN', 'D': 'zh-TW', 'E': 'zh-TW', 'F': 'zh-HK', 'G': 'ko-KR', 'H': 'fr-FR', 'I': 'es-ES', 'J': 'it-IT', 'K': 'nl-NL', 'L': 'ja-JP'}
langCodeKey = list(targetLangCode.keys())
keyList = []
valueList = []
json_dict = {}

# Column name : language code
# B : EN
# C : SCN
# D : TCN
# E : TW
# F : HK
# G : KR
# H : FR
# I : SP
# J : IT
# K : NL (dutch)
# L : JP

for row in loadedSheet['A']:
    keyList.append(row.value)

for element in langCodeKey:
    for row in loadedSheet[element]:
        valueList.append(row.value)
    json_dict = dict(zip(keyList, valueList))
    valueList = []
    del (json_dict[keyList[0]])
    with open('../assets/' + targetLangCode[element] + '.json', 'w', encoding='UTF-8') as outfile:
        json.dump(json_dict, outfile, ensure_ascii=False)
        print('Done with ' + targetLangCode[element])