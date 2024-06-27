def formatFloat(n):
    x=str(round(n,2))
    z=len(x)
    n=0
    for y in x:
        if y=='.':
            if z-n==2:
                x=x+'0'
                return x
            return x
        n=n+1
    return x+'.00'
print(formatFloat(100.1))