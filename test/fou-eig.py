def generateOrdinalNumber(number):
    if number<101:
        if number==1:
            return '1st'
        elif number==2:
            return '2nd'
        elif number==3:
            return '3rd'
        elif number>3 and number<20:
            return str(number)+'th'
        elif number>20 and number<101:
            n=number%10
            if n==0:
                return str(number)+'th'
            elif n==1:
                return str(number)+'st'
            elif n==2:
                return str(number)+'nd'
            elif n==3:
                return str(number)+'rd'
            elif n>3 and n<10:
                return str(number)+'th'
    else:
        numbers=number
        number=number%100
        if number==1:
            return str(numbers)+'st'
        elif number==2:
            return str(numbers)+'nd'
        elif number==3:
            return str(numbers)+'rd'
        elif number>3 and number<20:
            return str(numbers)+'th'
        elif number>20 and number<101:
            n=number%10
            if n==0:
                return str(numbers)+'th'
            elif n==1:
                return str(numbers)+'st'
            elif n==2:
                return str(numbers)+'nd'
            elif n==3:
                return str(numbers)+'rd'
            elif n>3 and n<10:
                return str(numbers)+'th'
print(generateOrdinalNumber(9999))