#集合運算
s={3,4,5}
print(5 in s)
a={4,8,11}
x=s&a #交集&
print(x) 
x=s|a #聯集|
print(x) 
x=s-a #差集-
print(x) 
x=s^a #反交集^
print(x)
y=set('apple') #set 字串變集合
print(y)
#字典運算
z={'apple':'蘋果','bug':'蟲'}
print('apple' in z)
del z['apple'] #刪除
print(z)
z={x:x+1 for x in s} #字典運算
print(z)