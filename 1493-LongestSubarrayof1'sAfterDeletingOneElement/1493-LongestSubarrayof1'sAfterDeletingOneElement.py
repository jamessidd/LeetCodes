class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        maxcount = 0
        dels = 1
        for right in range(len(nums)):

            if nums[right] == 0:
                dels -= 1
            
            while dels < 0:
                if nums[left] == 0:
                    dels += 1
                left += 1
            
            maxcount = max(maxcount, right - left)
        return maxcount