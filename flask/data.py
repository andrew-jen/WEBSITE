import pymongo
import certifi #確保ssl為最新的
from pymongo import MongoClient 
from flask import Flask
from flask import request
from flask import redirect
import json
from flask import render_template
from flask import session
app=Flask(
    __name__,
    static_folder='travel', #資料夾名稱，記得這裡+逗號
    static_url_path='/andrew' #網址路徑(http://127.0.0.1:3000/andrew/01.JPG)，如果改成'/'，這樣網址就變成http://127.0.0.1:3000/01.JPG
)

app.secret_key='secretkey' #使用session必須設定secret key
uri =  "mongodb+srv://a0988398645:a0910035817@andrew.3xi60lp.mongodb.net/?retryWrites=true&w=majority&appName=andrew"

# 創建客戶端並連接到伺服器
client = MongoClient(uri, tlsCAFile=certifi.where())

# 發送 ping 以確認成功連接
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")

db = client.member
collection = db.members
collection.insert_one({'venue': '松菸文創園區', '剩餘名額': 24,'date':'6/1'})
collection.insert_one({'venue': '中正運動中心', '剩餘名額': 28,'date':'6/2'})
collection.insert_one({'venue': '大安運動中心', '剩餘名額': 32,'date':'6/8'})
collection.insert_one({'venue': '松菸文創園區', '剩餘名額': 24,'date':'6/9'})
collection.insert_one({'venue': '松菸文創園區', '剩餘名額': 24,'date':'6/15'})
collection.insert_one({'venue': '大安運動中心', '剩餘名額': 32,'date':'6/16'})
collection.insert_one({'venue': '仁愛國中', '剩餘名額': 8,'date':'6/22'})
collection.insert_one({'venue': '松菸文創園區', '剩餘名額': 24,'date':'6/23'})
collection.insert_one({'venue': '中正動中心', '剩餘名額': 28,'date':'6/29'})
collection.insert_one({'venue': '松菸文創園區', '剩餘名額': 24,'date':'6/30'})