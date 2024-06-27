def fill(words, value):
    list=[]
    for x in words:
        if x !="":
            list.append(x)
        else:
            list.append(value)
    return list