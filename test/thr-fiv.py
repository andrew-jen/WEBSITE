def getPassRate(grades):
    p=[]
    n=len(grades)
    for x in grades:
        if x>=60:
            p.append(x)
    l=len(p)
    r=int(l/n*100)
    return str(r)+'%'
print(getPassRate([70, 0, 33, 60, 2, 59]))