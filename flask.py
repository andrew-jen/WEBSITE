from flask import Flask
app=Flask(__name__) #__name__目前執行的模組為主程式或其他程式

@app.route('/') #函式的裝飾(decorator)，此處為網站目錄/路徑
def home():
    return 'hello'

@app.route('/test') #網站分頁
def test():
    return 'test'

if __name__=='__main__': #如果以主程式執行
    app.run() #執行伺服器

#將檔案傳到雲端執行:
  #1. 建立runtime.txt檔，內容:python-3.9.0(使用的版本)
  #2. 建立requirements.txt檔，內容:Flask 換行 gunicorn 
  #3. 建立Procfile，內容:web gunicorn flask(檔名):app(變數名)
  #4. 使用命令heroku login登錄，然後git init，再來 heroku git:remote -a python-test-jen(python-test-jen是專案名) ，使用git add . 命令 ，使用git commit -m "First Deploy" ，