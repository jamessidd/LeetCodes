class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = ''
        i = len(words) - 1
        while i >= 0:
            res += words[i] + ' '
            i -= 1
            
        return res[0:len(res) - 1]
