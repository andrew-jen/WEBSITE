def isOverlapping(range1, range2):
    a=set(range(range1[0],range1[1]))|{range1[1]}
    b=set(range(range2[0],range2[1]))|{range2[1]}
    if a&b:
        return True
    else:
        return False

print(isOverlapping([5, 10],[9, 11]))