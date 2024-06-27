def checkArithmeticSequence(nums):
    dif=nums[1]-nums[0]
    n=0
    for x in nums:
        if n*dif+nums[0]==x:
            n=n+1
        else:
            return False
    return True
print(checkArithmeticSequence([3, 2, 1]))