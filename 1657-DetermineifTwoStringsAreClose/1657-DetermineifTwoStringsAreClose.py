class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1freq = dict()
        word2freq = dict()

        for i, char in enumerate(word1):
            word1freq[char] = word1freq.get(char, 0) + 1
        for i, char in enumerate(word2):
            word2freq[char] = word2freq.get(char, 0) + 1

        word1keys = set(word1freq.keys())
        word2keys = set(word2freq.keys())
        if word2keys != word1keys:
            return False
        word1vals = sorted(word1freq.values())
        word2vals = sorted(word2freq.values())
        return word1vals == word2vals

