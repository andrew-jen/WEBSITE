def checkMoney(x):
    # 你的程式碼
    x=int(input('請輸入正整數:'))
    if x>=100 and x<=100000 and x%100==0:
        return True
    return False
checkMoney(30)
checkMoney(2000)
checkMoney(6150)