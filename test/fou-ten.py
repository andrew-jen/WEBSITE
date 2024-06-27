def isOverlapping(rect1, rect2):
    x1=set(range(rect1[0],rect1[0]+rect1[2]+1))
    x2=set(range(rect2[0],rect2[0]+rect2[2]+1))
    y1=set(range(rect1[1]-rect1[3],rect1[1]+1))
    y2=set(range(rect2[1]-rect2[3],rect2[1]+1))
    if x1&x2:
        if y1&y2:
            return True
    return False
    
print(isOverlapping([0, 0, 10, 10],[-5, 5, 5, 5]))