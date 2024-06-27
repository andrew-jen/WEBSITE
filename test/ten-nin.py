def countWords(s):
    n=0
    if s != '':
        for x in s:
            if x==' ':
                n=n+1
        return n+1
    else:
        return 0
print(countWords(''))
    