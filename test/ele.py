def findIndex(nums, target):
    n=1
    for x in nums:
        if x==target:
            return n
        else:
            n=n+1
    return -1
