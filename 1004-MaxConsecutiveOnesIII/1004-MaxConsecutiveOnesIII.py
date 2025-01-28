class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        maxcount = 0
        for right in range(len(nums)): 

            if nums[right] == 0:
                k -= 1 #use a flip

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            maxcount = max(maxcount, right - left + 1)

        return maxcount
        