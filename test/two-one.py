def findMaxZero(nums):
    max_zeros = 0  # 用于记录最大连续0的数量
    current_zeros = 0  # 用于记录当前连续0的数量
    
    for num in nums:
        if num == 0:
            current_zeros += 1
        else:
            max_zeros = max(max_zeros, current_zeros)  # 更新最大连续0的数量
            current_zeros = 0  # 重置当前连续0的数量
    
    return max_zeros