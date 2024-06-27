def getOverlappingRange(range1, range2):
    x=set(range(range1[0],range1[1]+1))
    y=set(range(range2[0],range2[1]+1))
    if x&y:
        if len(list(x&y))>1:
            return list(x&y)
        else:
            z=list(x&y)
            z.append(z[0])
            return z
    else:
        return []
    
print(getOverlappingRange([-5, 5],[-6, -5]))