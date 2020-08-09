class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s

        while True:
            is_good = True
            for i in range(len(ans)-1):
                if ans[i].swapcase() == ans[i+1]:
                    ans = ans[:i] + ans[i+2:]
                    is_good = False
                    break
            if is_good:
                break
        return ans