#break
n=1
while n<5:
    n=n+1
    if n==3:
        break
print(n)

#continue
z=0
for x in [0,1,2,3]:
    if x%2==0:
        continue
    print(z)
    z=z+1  
else:
    print(z)

#找出平方根
x=float(input('正整數: '))
y=x**0.5
print(y)

x=int(input('正整數: '))
for y in range(x):
    if y*y==x:
        print(y)
        break
else:
    print('no')

#sum
n=1
x=3
y=4
while n<5:
    n=n+1
    z=x+y
    x=y
    y=z
    print(z)
else:
    print(z)