def getFibNumber(n):
    n1=1
    n2=1
    n=n-1
    z=0
    if n>0:
        while z<n:
            x=n1+n2
            n1=n2
            n2=x
            z=z+1
    else:
        return 1
    return x
print(getFibNumber(0))