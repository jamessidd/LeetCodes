class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:

            if char == '*':
                stack.pop()
                continue
            stack.append(char) 
        res = ''
        for char in stack:
            res += char
        return res