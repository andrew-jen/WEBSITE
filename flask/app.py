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
def home():
    print('方法:',request.method)
    print('通訊協定:',request.scheme)
    print('主機名稱:',request.host)
    print('路徑:',request.path)
    print('網址:',request.url)
    print('瀏覽器和作業系統:',request.headers.get('user-agent')) #headers標籤
    print('語言偏好:',request.headers.get('accept-language'))
    print('引薦網址:',request.headers.get('referrer'))
    lang=request.headers.get('accept-language')
    if lang.startswith('zh'): #zh是中文
        return '你好'
    else:
        return 'hi'

@app.route('/user/<name>')
def index(name):
    return 'hi '+name

@app.route('/sum')
def sum():
    max=int(request.args.get('max',101)) #預設值100,args是要求字串
    add=0
    for x in range(0,max):
        add+=x
    return str(add) #回應前端以字串呈現

#後端回應前端的方式(回應字串、回應json字串、redirect、樣板引擎)
@app.route('/page1')
def dic():
    return json.dumps({'apple':'蘋果','orange':'橘子'},ensure_ascii=False) #json.dumps轉換成json格式的字典,ensure_ascii=False確保不使用assci編碼處理中文
    #return redirect('/') #記得import redirect，可以講網頁直接轉連接到本網址的/根目錄，也可以把('/')改成其他網址

#樣板引擎
@app.route('/page2')
def word():
    #return render_template('word',name='andrew') #word是檔案名稱，檔案必須放在名為templates(有s)的子資料夾中，記得前面先from flask import
    return render_template('index.html') #使用html檔建立前端網頁畫面

#表單/輸入框互動(詳見html)
@app.route('/page3')
def list():
    name=request.args.get('n')
    session['jen']=name #session可以儲存使用者輸入的資料，['jen']裡面的文字可以任意(記得先from flask import，並且先設定secret key)
    return '您好 '+name

@app.route('/page4')
def feedback():
    name=session['jen'] #取出session資料
    return name+' 很高興認識你'

#連線方式有好幾種，最常用get和post(僅限使用表單時，有不適合公開在網址上的資料用post)，沒特別設定時默認為get
#@app.route('/page3',methods=['POST])
#def list():
    #return '您好 '+request.form('n')
#html上也要同步調整為<form action="page3"> methods='POST'>

app.run(port=3000) #port主機名