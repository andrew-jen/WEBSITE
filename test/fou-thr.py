def upperCamelToSnake(name):
    d={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
    n1=-1
    n2=0
    a=name[0].lower()+name[1:]
    b=''
    for x in a:
        if x.isupper():
            a=a[0:n2]+a[n2].lower()+a[n2+1:]
            b=b+a[n1+1:n2]+'_'
            n1=n2-1
            n2=n2+1
        else:
            n2=n2+1
    b=b+a[n1+1:]
    return b

print(upperCamelToSnake("GetWeatherData"))
   