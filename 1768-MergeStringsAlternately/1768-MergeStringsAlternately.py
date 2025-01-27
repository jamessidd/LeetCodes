class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ''
        i = 0
        while i < len(word1) and i < len(word2):

            res += word1[i]
            res += word2[i]
            i += 1

        if word1:
            res += word1[i:len(word1)]
        if word2:
            res += word2[i:len(word2)]
        return res