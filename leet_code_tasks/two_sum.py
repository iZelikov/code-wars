def twoSum(nums, target):
    for i,x in enumerate(nums):
        for j in range(i):
            if nums[i]+nums[j] == target and i!=j:
                return [i,j]
    return False

print(twoSum(nums = [3,3],target= 6))