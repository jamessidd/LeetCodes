class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1:
            return nums

        right = 0
        left = 0
        while right < len(nums):

            if nums[right] != 0:
                #move non zero to place
                nums[left] = nums[right]
                left += 1

            right += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
        return nums