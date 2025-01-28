class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        currcount = sum([1 for char in s[:k] if char in vowels])
        maxcount = currcount

        for i in range(k, len(s)):

            if s[i - k] in vowels:
                currcount -= 1
            if s[i] in vowels:
                currcount += 1

            maxcount = max(maxcount, currcount)

        return maxcount

        return False
