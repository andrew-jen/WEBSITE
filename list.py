#可變動列表[]
grade=[60,30,20,15,70]
grade[0]=50 #取代
grade[1:4]=[] #刪除
print(grade)
grade=grade+[1,5]
print(grade)
print(len(grade)) #取得列表長度(多少筆資料)
data=[[5,10,15],[0,20,50]]
print(data[0][2])
#不可變動列表()

#要再另外學怎麼對列表內的數值運算