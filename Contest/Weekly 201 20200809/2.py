class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s_list = [""]*(n+2)
        
        def rec(n):
            if n == 1:
                s_list[n] = "0"
                return "0"
            elif s_list[n] != "":
                return s_list[n]
            else:
                s_n_1 = rec(n-1)
                s_n = s_n_1 + "1" + ("".join("1" if x == "0" else "0" for x in s_n_1))[::-1]
                # Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
                s_list[n] = s_n
                return s_n
        
        rec(n)
        return s_list[n][k-1]