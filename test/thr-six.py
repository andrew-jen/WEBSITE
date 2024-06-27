def findUnique(ns):
    n=0
    if ns[0]==ns[1]:
        for x in ns:
            if x != ns[0]:
                return n
            else:
                n=n+1
    elif ns[0] != ns[1]:
        if ns[0]==ns[2]:
            return 1
        else:
            return 0
            