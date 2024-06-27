def checkPassword(s):
    if len(s) < 8 or len(s) > 16:
        return False

    a={'!','@','#','$','%'}
    s=set(s)
    c={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    d={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    e={'0','1','2','3','4','5','6','7','8','9'}
    A=s&a
    C=s&c
    D=s&d
    E=s&e
    s2=s-a
    s2=s2-c
    s2=s2-d
    s2=s2-e
    if s2:
        return False

    if A:
        if C:
            if D:
                if E:
                    return True
    return False

print(checkPassword('1aB@1111111111'))