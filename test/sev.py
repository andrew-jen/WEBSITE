def toCSVString(nums):
    if nums==None:
        return '空字串'
    else:
        z=0
        n=len(nums)
        x=''
        while z<n:
            y=str(nums[z])
            x=x+str(y)+','
            z=z+1
        x=x[:-1]
        return x

print(toCSVString([3, 5, -4, 2]))
