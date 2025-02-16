class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        maxvol = 0
        while left < right:

            width = right - left
            volume = width * min(height[left], height[right])
            maxvol = max(volume, maxvol)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return maxvol
        