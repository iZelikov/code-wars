# brute force variant

# def twoSum(nums, target):
#     for i,x in enumerate(nums):
#         for j in range(i):
#             if nums[i]+nums[j] == target and i!=j:
#                 return [i,j]
#     return False

# sorted list variant

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid  # возвращаем индекс найденного элемента
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1  # если элемент не найден
#
# def twoSum(nums, target):
#     sorted_nums  = sorted(nums)
#     reversed_rums = nums[::-1]
#     for i in range(len(sorted_nums)):
#         j = binary_search(sorted_nums, target - sorted_nums[i])
#         if j >=0 and i!=j:
#             return [nums.index(sorted_nums[i]), len(nums) -1 - reversed_rums.index(sorted_nums[j])]
#     return False

# hash-map variant
# Не работает, спотыкается на числах, равных половине таргета

# def twoSum(nums, target):
#     d_nums = {x:i for i,x in enumerate(nums)}
#     for key,first_index in d_nums.items():
#         second_index = d_nums.get(target-key)
#         if second_index is not None:
#             if first_index != second_index:
#                 return [first_index, second_index]
#             else:
#                 second_index = nums.index(target-key)
#                 return [first_index, second_index]
#     return False

# правильный hash-map variant
def twoSum(nums, target):
    nums_dict = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in nums_dict:
            return [nums_dict[diff], index]
        else:
            nums_dict[value] = index
    return False


print(twoSum(nums = [1,3,3,-134,567],target= 6))