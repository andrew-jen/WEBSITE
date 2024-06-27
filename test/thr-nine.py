def removeDuplicates(ns):
    l=[]
    for x in ns:
        if x not in l:
            l.append(x)
    return l
