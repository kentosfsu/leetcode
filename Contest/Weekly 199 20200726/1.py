"""
1528. Shuffle String
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.
"""
class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        current_state = "0"
        count = 0
        for c in target:
            # different state, then flip numbers for following digits
            if c != current_state:
                count += 1
                current_state = c
            else:
                continue
        return count