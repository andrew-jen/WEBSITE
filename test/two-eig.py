def comparePokerFigure(f1, f2):
    if f1=='A':
        f1=14
    elif f1=='K':
        f1=13
    elif f1=='Q':
        f1=12
    elif f1=='J':
        f1=11
    if f2=='A':
        f2=14
    elif f2=='K':
        f2=13
    elif f2=='Q':
        f2=12
    elif f2=='J':
        f2=11
    
    f1=int(f1)
    f2=int(f2)

    if f1>f2:
        return True
    else:
        return False
    
print(comparePokerFigure('K','10'))