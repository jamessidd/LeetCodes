class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        currsum = sum(nums[:k])
        maxsum = currsum

        for i in range(k, len(nums)):

            currsum -= nums[i - k]
            currsum += nums[i]
            maxsum = max(maxsum, currsum)

        return maxsum / float(k)