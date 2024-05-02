x=input('輸入數字: ')
x=int(x)
if x>20:
    print('yes')
elif x>10:
    print('10')
else:
    print('no')
    
n1=float(input('輸入數字: '))
n2=float(input('輸入數字: '))
op=input('符號 +,-,*,/ : ')
if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='*':
    print(n1*n2) 
elif op=='/':
    print(n1/n2)
else:
    print('不支援')