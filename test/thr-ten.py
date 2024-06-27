def addHours(current, offset):
    if current+offset<24 and current+offset>0:
        return current+offset
    elif current+offset>23:
        x=(current+offset)%24
        return x
    elif current+offset<1:
        x=(current+offset)%24
        return x
    
print(addHours(1,-5))