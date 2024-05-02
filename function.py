#def
def calculation(n,x,y):
    while n<5:
        n=n+1
        z=x+y
        x=y
        y=z
        print(z)
    else:
        print(z)
calculation(0,7,18)

#無限參數*
def num(*n): # *n是一個list
    print(n)
num(1,2,3)
num(4,5)

def num(*c): 
    sum=0
    for b in c:
        sum=sum+b
    else:
        print(sum/len(c))
num(1,2,3)
num(4,5)