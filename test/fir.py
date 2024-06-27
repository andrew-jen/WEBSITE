"""
    @param s:{String}
    @return :{Boolean}
"""
def checkHTTPS(s):
    # 你的程式碼
    if s[0]=='h' or s[0] =='H':
        if s[1]=='t' or s[1] =='T':
            if s[2]=='t' or s[2] =='T':
                if s[3]=='p' or s[3] =='P':
                    if s[4]=='s' or s[4] =='S':
                        if s[5]==':':
                            if s[6]=='/':
                                if s[7]=='/':
                                    return True
    return False
        

s='https://test.com/'
print(checkHTTPS(s))

s='h12345678'
print(checkHTTPS(s))

s='HTTPs://test.com/'
print(checkHTTPS(s))