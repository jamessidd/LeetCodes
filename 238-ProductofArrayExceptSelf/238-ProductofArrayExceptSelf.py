class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        i = len(nums)
        postfix = 1
        while i > 0:
            i -= 1
            res[i] *= postfix
            postfix *= nums[i]
        return res

        