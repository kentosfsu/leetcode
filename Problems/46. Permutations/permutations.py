class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.generate(res, set(nums), [])
        return res
    
    def generate(self, res, remain, subset):
        if not remain:
            res.append(subset)
            return
        print(remain)
        for num in remain:
            self.generate(res, remain-{num}, subset+[num])
            