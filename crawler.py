import urllib.request as request
x='https://www.ptt.cc/bbs/Gossiping/index.html'
req=request.Request(x,headers={
    'cookie':'over18=1',  #cookie是某些網站的驗證程序，在此為是否滿18歲
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
#req此變數在request連線系統下加入Request函式(它是HTTP client 函式庫)，此函式中有兩個參數，第一位為網址，第二位為User-Agent(這是偽裝一般訪客的必須資料，可於網站右上角-更多工具-開發人員工具-network-headers-Request Headers-User-Agent取得資料)
with request.urlopen(req) as y:
    data=y.read().decode('utf-8')
print(data)

import bs4
a=bs4.BeautifulSoup(data,'html.parser') # bs4.BeautifulSoup(data,'html.parser')除了data以外都是固定的
b=a.find_all('div',class_='title') #尋找所有class是title的div標籤
for title in b:
    if title.a != None: #如果標題a的內容不等於空的
        print(title.a.string)

link=a.find('a',string='‹ 上頁') #尋找內容是‹ 上頁的a標籤
print(link['href'])

#重複不斷抓取上頁的資料
import urllib.request as request
def everying(x):
    req=request.Request(x,headers={
    'cookie':'over18=1',  #cookie是某些網站的驗證程序，在此為是否滿18歲
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

    with request.urlopen(req) as y:
        data=y.read().decode('utf-8')

    import bs4
    a=bs4.BeautifulSoup(data,'html.parser') 
    b=a.find_all('div',class_='title') 
    for title in b:
        if title.a != None: 
            print(title.a.string)

    link=a.find('a',string='‹ 上頁')
    return link['href']

x='https://www.ptt.cc/bbs/Gossiping/index.html'
n=1
while n<5:
    n=n+1
    x='https://www.ptt.cc'+everying(x) #回傳值+同步執行???
    