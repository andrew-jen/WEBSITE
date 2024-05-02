#隨機選取
import random
x=random.choice([1,2,3,4,5,6,7,8,9])
print(x)

x=random.sample([1,2,3,4,5,6,7,8,9],3) #隨機取3個(或多個)
print(x)

data=[5,10,15,20,25]
random.shuffle(data) #隨機調換list順序
print(data)

data=random.uniform(1.5,111.3) #隨機取得亂數
data=int(data)
print(data)

n=0
while n<5:
    n=n+1
    data=random.uniform(1.5,111.3) #隨機取得亂數
    data=int(data)
    print(data)
    if n==4:
        break

data=random.normalvariate(60,10) #normalvariate常態分配亂數，60是平均數/10是標準差
print(data)

#統計模組
import statistics as s #(別名)
data=s.mean([5,10,15,20]) #mean平均數
print(data)

data=s.median([2,5,15,100]) #median中位數(去掉最大最小值)
print(data)

data=s.stdev([5,10,15,20]) #stdev標準差
print(data)