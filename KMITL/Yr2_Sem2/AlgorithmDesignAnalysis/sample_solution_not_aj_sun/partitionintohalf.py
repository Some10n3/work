def canPartition(nums) -> bool:
    if sum(nums) % 2:
        return False
    
    dp = set()
    dp.add(0)
    target = sum(nums) // 2
    
    for i in range(len(nums)):
        new_dp = set()
        for j in dp:
            if (j + nums[i]) == target:
                return True
            new_dp.add(j + nums[i])
            new_dp.add(j)
        dp = new_dp
    return True if target in dp else False

print(canPartition([1, 5, 11, 5])) # True