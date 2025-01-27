class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first = float('INF')
        second = float('INF')

        for i, num in enumerate(nums):

            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False 