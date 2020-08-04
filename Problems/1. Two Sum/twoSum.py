"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        d = {} # num: index
        
        for i, num in enumerate(nums):
            num_wanted = target - num
            if num_wanted in num_dict:
                return [d[num_wanted], i]
            else:
                d[num] = i
        raise ValueError('No solution found!')