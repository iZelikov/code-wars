"""
1. Two Sum
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        subs = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in subs:
                return i, subs[sub]
            else:
                subs[nums[i]] = i

