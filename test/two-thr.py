def convertSeconds(sec):
    # 你的程式碼
    a=sec//86400
    A=sec%86400
    b=A//3600
    B=A%3600
    c=B//60
    d=B%60
    return [a,b,c,d]