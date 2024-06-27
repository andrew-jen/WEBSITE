def sumOfArithmeticSequence(min, max, differ):
    sum=min
    x=min
    while x<max:
        x=x+differ
        if x<=max:
            sum=sum+x
        else:
            return sum
    return sum
