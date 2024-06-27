def findSecond(nums):
    n=len(nums)
    z=0
    y=max(nums)
    while z<n:
        z+1
        if y in nums: 
            nums.remove(y)
        else:
            break
    value=max(nums)
    return value
print(findSecond([1, 3, 3, 2, 5, -2]))
print(findSecond([-5, -10, -8, 1, -1]))
print(findSecond([0, 2]))
print(findSecond([-2,1,1,1,0]))
