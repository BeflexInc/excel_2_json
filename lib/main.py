import json
from openpyxl import load_workbook

excelFile = input("Excel File location : ").strip()

loadedExcel = load_workbook(excelFile, data_only=True)

# 활성화된 시트 가져오기
loadedSheet = loadedExcel.active

# 새 언어 추가될때마다 주석 풀어주면 됨
targetLangCode = {'B': loadedSheet['B1'].value, 'C': loadedSheet['C1'].value, 'D': loadedSheet['D1'].value,
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
        valueList.append(row.value)
    json_dict = dict(zip(keyList, valueList))
    valueList = []
    # 첫 번째 row 의 언어 코드 row 지우기
    del (json_dict[keyList[0]])
    # 변환
    with open('./assets/' + str(targetLangCode[element]).lower() + '.json', 'w', encoding='UTF-8') as outfile:
        json.dump(json_dict, outfile, ensure_ascii=False, indent='\t')
        print('Done with ' + str(targetLangCode[element]).lower())
