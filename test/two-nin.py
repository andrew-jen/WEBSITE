def comparePokerCard(c1, c2):
    c1=list(c1)
    c2=list(c2) 

    if 'J' in c1:
        c1[0]=11
    elif 'Q' in c1:
        c1[0]=12
    elif 'K' in c1:
        c1[0]=13
    elif 'A' in c1:
        c1[0]=14

    c11=int(c1[0])
    
    if 'J' in c2:
        c2[0]=11
    elif 'Q' in c2:
        c2[0]=12
    elif 'K' in c2:
        c2[0]=13
    elif 'A' in c2:
        c2[0]=14

    c21=int(c2[0])

    if c11>c21:
        return True
    elif c21>c11:
        return False
    else:
        suit1 = 0
        suit2 = 0
        if 'C' in c1:
            suit1 = 1
        elif 'D' in c1:
            suit1 = 2
        elif 'H' in c1:
            suit1 = 3
        elif 'S' in c1:
            suit1 = 4          
        
        if 'C' in c2:
            suit2 = 1
        elif 'D' in c2:
            suit2 = 2
        elif 'H' in c2:
            suit2 = 3
        elif 'S' in c2:
            suit2 = 4
        
        if suit1>suit2:
            return True
        else:
            return False
        
print(comparePokerCard("3S","3H"))