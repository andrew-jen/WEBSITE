#擷取網路資料
import urllib.request as request
import json #要確認網站的資料格式是哪種
x='https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'
with request.urlopen(x) as y:
    data=json.load(y)
companylist=data["result"]["results"] #要看網站資料格式中"公司名稱"的位置
for company in companylist:
    print(company["公司名稱"])

with open('internet.text',mode='w',encoding='utf-8') as file: #取得"公司名稱"寫入text
    for company in companylist:
        file.write(company["公司名稱"]+'\n') #注意換行方式 +'\n'