class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)

            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()

            else:
                return False

        return not stack