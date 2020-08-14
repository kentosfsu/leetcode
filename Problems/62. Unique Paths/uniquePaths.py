class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # caluculate combinations (m-1+n-1)_C_(n-1)
        
        if m == 1 or n == 1:
            return 1
        
        def fact(n):
            if n == 1:
                return 1
            return n*fact(n-1)
        
        combinations = fact(m-1+n-1) / (fact(m-1)*fact(n-1))
        return combinations