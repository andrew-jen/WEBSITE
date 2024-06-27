def findMaxProduct(nums):
    n=len(nums)
    NUMS2=nums
    
    y=max(nums)
    x=min(NUMS2)

    nums.remove(y)
    
    value1=y*max(nums)
    
    
    NUMS2.remove(x)
    value2=x*min(NUMS2)   
    if value1 > value2:
        return value1
    else:
        return value2
    
print(findMaxProduct([2, -1, 0]))