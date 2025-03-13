import pymongo
import certifi #確保ssl為最新的
from pymongo import MongoClient 
from bson.objectid import ObjectId

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
db = client.member  # 創建一個名為 'num1' 的資料庫

from flask import Flask
from flask import request
from flask import redirect
import json
from flask import render_template
from flask import session

#影音、文字或其他檔案，可以直接上傳網路，透過建立子資料夾-static，可以用來存放靜態檔案資料，並默認網址為:主機/static/檔案名稱
#也可以修改網址路徑
app=Flask(
    __name__,
    static_folder='travel', #資料夾名稱，記得這裡+逗號
    static_url_path='/andrew' #網址路徑(http://127.0.0.1:3000/andrew/01.JPG)，如果改成'/'，這樣網址就變成http://127.0.0.1:3000/01.JPG
)

app.secret_key='secretkey' #使用session必須設定secret key

@app.route('/')
def index():
    session['cart1']=0
    session['cart2']=0
    session['cart3']=0
    return render_template('index.html')

@app.route('/member')
def member():
    session['name']=''
    session['email']=''
    session['account']=''
    session['password']=''
    return render_template('member.html')

@app.route('/user',methods=['POST'])
def user():
    name=request.form.get('name')
    email=request.form.get('email')
    account=request.form.get('account')
    password=request.form.get('password')
    session['name']=name #session可以儲存使用者輸入的資料，['jen']裡面的文字可以任意(記得先from flask import，並且先設定secret key)
    session['email']=email
    session['account']=account
    session['password']=password
    data={'name':name,'email':email,'account':account,'password':password}
    personal=db.personal
    result1=personal.find_one({'email':email})
    result2=personal.find_one({'account':account})
    
    
    if len(password) < 8 or len(password) > 16:
        return redirect('/erro?msg=密碼不符合規定')

    a={'!','@','#','$','%'}
    s=set(password)
    c={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    d={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    e={'0','1','2','3','4','5','6','7','8','9'}
    A=s&a
    C=s&c
    D=s&d
    E=s&e
    s2=s-a
    s2=s2-c
    s2=s2-d
    s2=s2-e
    if s2:
        return redirect('/erro?msg=密碼不符合規定')

    if A:
        if C:
            if D:
                if E:
                    print(password)
                    if result1 != None:
                        return redirect('/erro?msg=信箱已被註冊')
                    elif result2 != None:
                        return redirect('/erro?msg=帳號已被註冊')
                    else:
                        cart=db.cart
                        inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
                        n1=inv['勝利']
                        n2=inv['暴力丹']
                        n3=inv['江山燕']
                        inventory={'n1':n1,'n2':n2,'n3':n3}
                        number=[]
                        members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
                        personal.insert_one({'name':name,'email':email,'account':account,'password':password})
                        return render_template('user.html',data=data,members=members,inventory=inventory) #第一個data是字典data，第二個data是html的data

    return redirect('/erro?msg=密碼不符合規定')

@app.route('/users',methods=['POST'])
def users():
    productions=db.productions
    personal=db.personal
    if session['account'] == '':
        account=request.form.get('account')
        password=request.form.get('password')
        print(account)
        session['account']=account
        session['password']=password
    account=session['account']
    password=session['password']
    result1=personal.find_one({'password':password})
    result2=personal.find_one({'account':account})
    canclecart=request.form.get('sure')

    cart=db.cart
    inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
    n1=inv['勝利']
    n2=inv['暴力丹']
    n3=inv['江山燕']
    buy1=request.form.get('buy1')
    buy2=request.form.get('buy2')
    buy3=request.form.get('buy3')
    inventory={'n1':n1,'n2':n2,'n3':n3}
    
    
    number=[]
    venue=db.members
    times=venue.find()
    for doc in times:
        doc=int(doc['剩餘名額'])
        number.append(doc)
        
    num1=request.form.get('num1')
    num2=request.form.get('num2')
    num3=request.form.get('num3')
    num4=request.form.get('num4')
    num5=request.form.get('num5')
    num6=request.form.get('num6')
    num7=request.form.get('num7')
    num8=request.form.get('num8')
    num9=request.form.get('num9')
    num10=request.form.get('num10')

    inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
    n1=inv['勝利']
    n2=inv['暴力丹']
    n3=inv['江山燕']
    inventory={'n1':n1,'n2':n2,'n3':n3}
    members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number}
    if result1 == None:
        return redirect('/erro?msg=密碼錯誤')
    elif result2 == None:
        return redirect('/erro?msg=帳號錯誤')
    else:
        name=result1['name']
        session['name']=name
        name=session['name']
        account=session['account']
        password=session['password']
    
    if num1 != None :
        number=[]
        num1=int(num1)
        venue.update_one({'date':'6/1'},{'$inc':{'剩餘名額':-num1}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num1<=4 and num1>=1 and number[0]>=0:
            name=session['name']
            venue.update_one({'date':'6/1'},{'$set':{name:str(num1)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/1'},{'$inc':{'剩餘名額':num1}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num2 != None :
        number=[]
        num2=int(num2)
        print(num2)
        venue.update_one({'date':'6/2'},{'$inc':{'剩餘名額':-num2}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num2<=4 and num2>=1 and number[1]>=0:
            name=session['name']
            venue.update_one({'date':'6/2'},{'$set':{name:str(num2)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/2'},{'$inc':{'剩餘名額':num2}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num3 != None :
        number=[]
        num3=int(num3)
        venue.update_one({'date':'6/8'},{'$inc':{'剩餘名額':-num3}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num3<=4 and num3>=1 and number[2]>=0:
            name=session['name']
            venue.update_one({'date':'6/8'},{'$set':{name:str(num3)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/8'},{'$inc':{'剩餘名額':num3}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num4 != None :
        number=[]
        num4=int(num4)
        venue.update_one({'date':'6/9'},{'$inc':{'剩餘名額':-num4}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num4<=4 and num4>=1 and number[3]>=0:
            name=session['name']
            venue.update_one({'date':'6/9'},{'$set':{name:str(num4)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/9'},{'$inc':{'剩餘名額':num4}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num5 != None :
        number=[]
        num5=int(num5)
        venue.update_one({'date':'6/15'},{'$inc':{'剩餘名額':-num5}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num5<=4 and num5>=1 and number[4]>=0:
            name=session['name']
            venue.update_one({'date':'6/15'},{'$set':{name:str(num5)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/15'},{'$inc':{'剩餘名額':num5}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num6 != None :
        number=[]
        num6=int(num6)
        venue.update_one({'date':'6/16'},{'$inc':{'剩餘名額':-num6}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num6<=4 and num6>=1 and number[5]>=0:
            name=session['name']
            venue.update_one({'date':'6/16'},{'$set':{name:str(num6)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/16'},{'$inc':{'剩餘名額':num6}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num7 != None :
        number=[]
        num7=int(num7)
        venue.update_one({'date':'6/22'},{'$inc':{'剩餘名額':-num7}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num7<=4 and num7>=1 and number[6]>=0:
            name=session['name']
            venue.update_one({'date':'6/22'},{'$set':{name:str(num7)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/22'},{'$inc':{'剩餘名額':num7}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num8 != None :
        number=[]
        num8=int(num8)
        venue.update_one({'date':'6/23'},{'$inc':{'剩餘名額':-num8}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num8<=4 and num8>=1 and number[7]>=0:
            name=session['name']
            venue.update_one({'date':'6/23'},{'$set':{name:str(num8)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/23'},{'$inc':{'剩餘名額':num8}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num9 != None :
        number=[]
        num9=int(num9)
        venue.update_one({'date':'6/29'},{'$inc':{'剩餘名額':-num9}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num9<=4 and num9>=1 and number[8]>=0:
            name=session['name']
            venue.update_one({'date':'6/29'},{'$set':{name:str(num9)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/29'},{'$inc':{'剩餘名額':num9}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
    elif num10 != None :
        number=[]
        num10=int(num10)
        venue.update_one({'date':'6/30'},{'$inc':{'剩餘名額':-num10}})
        times=venue.find()
        for doc in times:
            doc=int(doc['剩餘名額'])
            number.append(doc)
        if num10<=4 and num10>=1 and number[9]>=0:
            name=session['name']
            venue.update_one({'date':'6/30'},{'$set':{name:str(num10)}})
            data={'name':name}
            print(number)
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            venue.update_one({'date':'6/30'},{'$inc':{'剩餘名額':num10}})
            times=venue.find()
            for doc in times:
                doc=int(doc['剩餘名額'])
                number.append(doc)
            return redirect('/erro?msg=超過人數限制')
        
    elif canclecart == 'cancle':
        productions.delete_one({'details':session['details'],'name':session['name']})
        session['details']=''
        if session['cart1']!=0:
            cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'勝利':session['cart1']}})
            session['cart1']=0
        if session['cart2']!=0:
            cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'暴力丹':session['cart2']}})
            session['cart2']=0
        if session['cart3']!=0:
            cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'江山燕':session['cart3']}})
            session['cart3']=0

    elif canclecart == 'ensure':
        session['cart1']=0
        session['cart2']=0
        session['cart3']=0
        
    elif buy1 != None:
        buy1=int(buy1)
        cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'勝利':-buy1}})
        inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
        n1=inv['勝利']
        n2=inv['暴力丹']
        n3=inv['江山燕']
        if n1>=buy1:
            session['cart1']=session['cart1']+buy1
            inventory={'n1':n1,'n2':n2,'n3':n3}
            data={'name':name}
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'勝利':buy1}})
            inventory={'n1':n1,'n2':n2,'n3':n3}
            data={'name':name}
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return redirect('/erro?msg=庫存不足')
        
    elif buy2 != None:
        buy2=int(buy2)
        cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'暴力丹':-buy2}})
        inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
        n1=inv['勝利']
        n2=inv['暴力丹']
        n3=inv['江山燕']
        if n2>=buy2:
            session['cart2']=session['cart2']+buy2
            inventory={'n1':n1,'n2':n2,'n3':n3}
            data={'name':name}
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'暴力丹':buy2}})
            inventory={'n1':n1,'n2':n2,'n3':n3}
            data={'name':name}
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return redirect('/erro?msg=庫存不足')
        
    elif buy3 != None:
        buy3=int(buy3)
        cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'江山燕':-buy3}})
        inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
        n1=inv['勝利']
        n2=inv['暴力丹']
        n3=inv['江山燕']
        if n3>=buy3:
            session['cart3']=session['cart3']+buy3
            inventory={'n1':n1,'n2':n2,'n3':n3}
            data={'name':name}
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return render_template('user.html',data=data,members=members,inventory=inventory)
        else:
            cart.update_one({'_id':ObjectId("665d8aeaa8a46f4fb4e6e80a")},{'$inc':{'江山燕':buy3}})
            inventory={'n1':n1,'n2':n2,'n3':n3}
            data={'name':name}
            members={'date1':'6/1','date2':'6/2','date3':'6/8','date4':'6/9','date5':'6/15','date6':'6/16','date7':'6/22','date8':'6/23','date9':'6/29','date10':'6/30','number':number,'name':name}
            return redirect('/erro?msg=庫存不足')
    
    inv=cart.find_one(ObjectId("665d8aeaa8a46f4fb4e6e80a"))
    n1=inv['勝利']
    n2=inv['暴力丹']
    n3=inv['江山燕']
    inventory={'n1':n1,'n2':n2,'n3':n3}
    data={'account':account,'password':password,'name':name}
    return render_template('user.html',data=data,members=members,inventory=inventory)
    
    
@app.route('/list')
def list():
    venue=db.members
    name=session['name']
    data={'name':name}
    paper1=venue.find({'date':'6/1'})
    for list1 in paper1:
        del list1['_id']
        del list1['venue']
        del list1['date']
        del list1['剩餘名額']
        list1=str(list1)
        list1=list1.replace('{','')
        list1=list1.replace('}','')
        list1=list1.replace("'",'')
    paper2=venue.find({'date':'6/2'})
    for list2 in paper2:
        del list2['_id']
        del list2['venue']
        del list2['date']
        del list2['剩餘名額']
        list2=str(list2)
        list2=list2.replace('{','')
        list2=list2.replace('}','')
        list2=list2.replace("'",'')
    paper3=venue.find({'date':'6/8'})
    for list3 in paper3:
        del list3['_id']
        del list3['venue']
        del list3['date']
        del list3['剩餘名額']
        list3=str(list3)
        list3=list3.replace('{','')
        list3=list3.replace('}','')
        list3=list3.replace("'",'')
    paper4=venue.find({'date':'6/9'})
    for list4 in paper4:
        del list4['_id']
        del list4['venue']
        del list4['date']
        del list4['剩餘名額']
        list4=str(list4)
        list4=list4.replace('{','')
        list4=list4.replace('}','')
        list4=list4.replace("'",'')
    paper5=venue.find({'date':'6/15'})
    for list5 in paper5:
        del list5['_id']
        del list5['venue']
        del list5['date']
        del list5['剩餘名額']
        list5=str(list5)
        list5=list5.replace('{','')
        list5=list5.replace('}','')
        list5=list5.replace("'",'')
    paper6=venue.find({'date':'6/16'})
    for list6 in paper6:
        del list6['_id']
        del list6['venue']
        del list6['date']
        del list6['剩餘名額']
        list6=str(list6)
        list6=list6.replace('{','')
        list6=list6.replace('}','')
        list6=list6.replace("'",'')
    paper7=venue.find({'date':'6/22'})
    for list7 in paper7:
        del list7['_id']
        del list7['venue']
        del list7['date']
        del list7['剩餘名額']
        list7=str(list7)
        list7=list7.replace('{','')
        list7=list7.replace('}','')
        list7=list7.replace("'",'')
    paper8=venue.find({'date':'6/23'})
    for list8 in paper8:
        del list8['_id']
        del list8['venue']
        del list8['date']
        del list8['剩餘名額']
        list8=str(list8)
        list8=list8.replace('{','')
        list8=list8.replace('}','')
        list8=list8.replace("'",'')
    paper9=venue.find({'date':'6/29'})
    for list9 in paper9:
        del list9['_id']
        del list9['venue']
        del list9['date']
        del list9['剩餘名額']
        list9=str(list9)
        list9=list9.replace('{','')
        list9=list9.replace('}','')
        list9=list9.replace("'",'')
    paper10=venue.find({'date':'6/30'})
    for list10 in paper10:
        del list10['_id']
        del list10['venue']
        del list10['date']
        del list10['剩餘名額']
        list10=str(list10)
        list10=list10.replace('{','')
        list10=list10.replace('}','')
        list10=list10.replace("'",'')
    document={'list1':list1,'list2':list2,'list3':list3,'list4':list4,'list5':list5,'list6':list6,'list7':list7,'list8':list8,'list9':list9,'list10':list10}
    return render_template('/list.html',data=data,document=document)

@app.route('/cancle')
def cancel():
    
    venue=db.members
    name=session['name']
    data={'name':name}
    date=request.args.get('cancle')
    num=venue.find_one({'date':date})
    print(name)
    for x in num:
        if x==name:
            print(101)
            num=int(num[name])
            change=venue.update_one({'date':date},{'$unset':{name:num}})
            numchange=venue.update_one({'date':date},{'$inc':{'剩餘名額':num}})
            return redirect('/list')
        else:
            print(x)
        
    return redirect('/')

@app.route('/backpack')
def backpack():
    write1=''
    write2=''
    write3=''
    if session['cart1'] != 0:
        write1='勝利羽球'+'----'+'數量:'+str(session['cart1'])+'價格:'+str(session['cart1']*450)   
    if session['cart2'] != 0:
        write2='暴力丹羽球'+'----'+'數量:'+str(session['cart2'])+'價格:'+str(session['cart2']*350)  
    if session['cart3'] != 0:
        write3='江山燕羽球'+'----'+'數量:'+str(session['cart3'])+'價格:'+str(session['cart3']*250)
    total=str(session['cart1']*450+session['cart2']*350+session['cart3']*250)
    cartlist={'list1':write1,'list2':write2,'list3':write3,'total':total}
    details=write1+write2+write3
    session['details']=details
    productions=db.productions
    productions.insert_one({'name':session['name'],'details':details,'sum':total})
    return render_template('backpack.html',cartlist=cartlist)
    
@app.route('/signin')
def signin():
    session['name']=''
    session['email']=''
    session['account']=''
    session['password']=''
    return render_template('signin.html')

@app.route('/erro')
def erro():
    message=request.args.get('msg','erro')
    return render_template('erro.html',message=message)

@app.route('/about')
def about():
    name=session['name']
    data={'name':name}
    return render_template('about.html',data=data)


app.run(port=3000) #port主機名
