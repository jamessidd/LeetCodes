class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 0
        postfix = sum(nums)
        for i in range(len(nums)):

            postfix -= nums[i]
            if prefix == postfix:
                return i
            prefix += nums[i]

        return -1
            
        