def findIndexes(nums, target):
    n=0
    list=[]
    for x in nums:
        if x==target:
            list.append(n)
            n=n+1
        else:
            n=n+1
    return list