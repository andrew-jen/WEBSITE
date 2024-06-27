def countKeywords(text, keyword):
    new=''
    for x in text:
        if x.isupper():
            new=new+x.lower()
        else:
            new=new+x

    l=''
    for x in keyword:
        if x.isupper():
            l=l+x.lower()
        else:
            l=l+x
    
    answer=new.split(l)
    return len(answer)-1

print(countKeywords( "abababazz","Aba"))