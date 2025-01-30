# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 0
        hi = n
        while True:
            
            mid = (lo + hi) // 2
            num = guess(mid)
            
            
            if num == 0:
                return mid
            elif num > 0:
                lo = mid + 1
            else:
                hi = mid

        return -1
        