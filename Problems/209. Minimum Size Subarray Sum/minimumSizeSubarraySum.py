class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        current_sum = 0
        min_count = len(nums)+1 #dummy
        i = 0
        
        for j in range(len(nums)):
            current_sum += nums[j]
            if current_sum >= s:
                while(current_sum - nums[i] >= s):
                    current_sum = current_sum - nums[i]
                    i += 1
                count = j-i+1
                min_count = min(min_count, count)
        
        if min_count == len(nums)+1: #if min_count did not updated at all
            return 0
        else:
            return min_count