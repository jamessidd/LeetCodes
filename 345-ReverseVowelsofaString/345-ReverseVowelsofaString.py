class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"

        res = ''
        left = 0
        right = len(s) - 1
        while left < len(s):

            if s[left] not in vowels:
                res += s[left]
            else:
                while right >= 0:
                    if s[right] in vowels:
                        res += s[right]
                        right -= 1
                        break
                    right -= 1
            left += 1
        return res
