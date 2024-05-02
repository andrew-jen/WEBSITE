#儲存檔案及寫入
with open('data.txt',mode='w',encoding='utf-8') as file: #encoding 是編碼，utf-8 是轉換中文的編碼模式
    file.write('你好\n很高興認識你')
#讀取檔案
with open('data.txt',mode='r',encoding='utf-8') as file: 
    data=file.read()
print(data)
#一行行讀取並加總
with open('data.txt',mode='w',encoding='utf-8') as file:
    file.write('0\n5\n10\n15')
sum=0
with open('data.txt',mode='r',encoding='utf-8') as file: 
    for x in file:
        sum=sum+int(x)
print(sum)
#使用json檔案
import json
with open('word.json',mode='w') as file:
    file.write('{\n"name":"andrew",\n"num":"2"\n}') #json的寫法，同下

import json
data = {
    'name': 'andrew',
    'num': '2'
}
with open('word.json',mode='w') as file:
    json.dump(data, file) #將python內容自動轉換成json

with open('word.json',mode='r') as file:
    data=json.load(file) #load將json內容轉換為字典型態
print('name',data['name'])

data['name']='jen' #修改json資料
with open('word.json',mode='w') as file:
    json.dump(data, file)
print('name',data['name'])