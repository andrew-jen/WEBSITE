def fill(words):
    list=[]
    s=""
    for x in words:
        if x !="":
            list.append(x)
            s=x
        else:
            list.append(s)
    return list

print(fill(["", "", "a"]))