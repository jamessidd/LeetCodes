class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [1] * len(nums)
        curr = 1

        for i, num in enumerate(nums):
            answer[i] *= curr
            curr *= num

        end = len(nums) - 1
        postfix = 1
        while end >= 0:

            answer[end] *= postfix
            postfix *= nums[end]
            end -= 1

        return answer
