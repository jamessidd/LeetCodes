class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        candiesset = set(candies)
        res = []
        for i, candy in enumerate(candies):
            
            if candy + extraCandies >= max(candiesset):
                res.append(True)
            else:
                res.append(False)
        return res