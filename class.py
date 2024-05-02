#類別class
class X:
    data=['andrew','sunny','leo']
    def file(y):
        if y not in X.data: #data要加x類別
            print('no')
        else:
            print('yes')
X.file('andrew') #呼叫類別

#實體物件
class X:
    def __init__(self,a,b): #定義函式(self固定要存在，但在後面的程式中直接忽略)
        self.a=a #(self.固定要存在，但在後面的程式中直接忽略)
        self.b=b
y=X(3,5) #y是變數或稱物件
print(y.a,y.b)

#實體方法
class X:
    def __init__(self,a,b): # a/b可以在外部取出
        self.a=a 
        self.b=b
        self.n=0
    def way(self,c,d): # c/d不可以在外部取出
        while self.n<5:
            self.n=self.n+1
            self.a=self.a*c
            self.b=self.b-d
            if self.n==5:
                break
        print(self.a+self.b)

z=X(2,11)
z.way(3,7)

#將檔案寫入及讀取的程式包裝到實體物件中
class file:
    def __init__(self,name):
        self.name=name
    def open(self,b):
        with open(self.name,mode='w',encoding='utf-8') as data:
            data.write(b)
    def read(self):
        with open(self.name,mode='r',encoding='utf-8') as x:
            print(x.read())

f1=file('nice')
f1.open('很好')
f1.read()

f2=file('data.txt')
f2.open('0\n5\n10\n15')
f2.read()