def checkPalindrome(s):
    s=list(s)
    while len(s)>1:   
        if s[0]==s[len(s)-1]:
            s.pop(0)
            s.pop()
        else:
            return False
    return True

print(checkPalindrome("a1aa"))