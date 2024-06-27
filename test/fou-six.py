def getChineseZodiac(year):
    map={0:'鼠',1:'牛',2:'虎',3:'兔',4:'龍',5:'蛇',6:'馬',7:'羊',8:'猴',9:'雞',10:'狗',11:'豬'}
    x=(year-1900)%12
    return map[x]