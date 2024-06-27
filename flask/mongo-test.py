import pymongo
import certifi #確保ssl為最新的
from pymongo import MongoClient 

# 替換為你的 MongoDB 連接字串和憑據(複製mongo網站-cluster-connect)
uri =  "mongodb+srv://a0988398645:a0910035817@andrew.3xi60lp.mongodb.net/?retryWrites=true&w=majority&appName=andrew"

# 創建客戶端並連接到伺服器
client = MongoClient(uri, tlsCAFile=certifi.where())

# 發送 ping 以確認成功連接
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")

# 把資料放進資料庫
db = client.num1  # 創建一個名為 'num1' 的資料庫
collection = db.number1  # 創建一個名為 'number1' 的集合
collection.insert_one({'name': 'andrew', 'gender': 'man'})  # 集合名.insert_one把資料新增到集合中
result=collection.insert_many([{'name': 'andrew', 'gender': 'man'},{'name': 'howerd', 'gender': 'man'}]) #insert_many一次新增多筆資料
print('資料新增成功')
print(result.inserted_ids) #取得資料在mongo資料庫上的編號

#取得mongo資料庫中的資料
print(collection.find_one()) #取得collection集合中的第一筆資料
from bson.objectid import ObjectId 
data=result.inserted_ids[0]
print(collection.find_one(data)) #透過資料編號取得collection集合中的指定資料(data為文件編號)，記得先載入ObjectId
print(collection.find_one(data)['_id']) #取得編號欄位的資料(編號欄固定為_id)
print(collection.find_one(data)['name']) #姓名欄

every=collection.find() #取出集合中的所有資料
for file in every:
    print(file['name']) #取出名稱欄資料

#更新文件資料
result=collection.update_one({'name':'andrew'},{'$set':{'name':'jen'}}) #更新一筆name為andrew的資料，並將name欄位更新為jen，('$set'用來更新或新增欄位，'$unset'可以清除欄位，'$inc'可以加減數值，若數字為2則加2，-2則減2，'$mul'可以乘除，若數值為2則乘2，0.5則除2)
print('符合條件的文件數',result.matched_count)
print('實際執行的文件數',result.modified_count)

result=collection.update_many({'name':'andrew'},{'$set':{'name':'jen'}}) #更新所有name為andrew的資料
print('符合條件的文件數',result.matched_count)
print('實際執行的文件數',result.modified_count)

#刪除資料
cancle=collection.delete_many({'name':'jen'}) #delete_one則是刪除一筆
print('實際刪除數量',cancle.deleted_count)

#篩選條件
data1=collection.find({'$and':[{'name':'andrew'},{'gender':'man'}]},sort=[('_id',pymongo.ASCENDING)]) #滿足所有條件，並依照id欄由小到大排序
data2=collection.find({'$or':[{'name':'andrew'},{'gender':'man'}]},sort=[('_id',pymongo.DESCENDING)]) #滿足任意條件，並依照id欄由大到小排序

for x in data1:
    print(x['name'])

for y in data2:
    print(y['_id'])



