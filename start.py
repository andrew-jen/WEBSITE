#字典
a={"apple":"蘋果"}
print(a["apple"])
#次方
b=2**3
print(b)
#整數法
c=5//6
print(c)
#開耕號
d=4**0.5
print(d)
#取餘數
e=4%3
print(e)
#字串
f='apple\'1\'' #跳脫
print(f)
print(a["apple"]+f)
f='apple\ngood' #換行
print(f)
f='''apple
111
222
good''' #換行
print(f)
g='hi '*3+'you'
print(g)
f='apple' #字串內的字母都有編號(a=0，l=3，e=4)
print(f[4]) #索引
print(f[0:4]) #索引一段區間(不含結尾)
print(f[0:]) 
print(f[:4]) 