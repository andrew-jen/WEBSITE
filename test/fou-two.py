def snakeToUpperCamel(name):
    c={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    a=name.split('_')
    n=0
    word=''
    for x in a:
        b=str(a[n][0])
        d=c[b]
        e=d+a[n][1:]
        word=word+e
        n=n+1
    return word
        


print(snakeToUpperCamel("hello_world"))