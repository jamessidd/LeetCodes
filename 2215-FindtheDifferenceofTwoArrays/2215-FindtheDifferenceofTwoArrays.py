class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1set = set(nums1)
        nums2set = set(nums2)

        res = [[],[]]

        for num in nums1set:
            if num not in nums2set:
                res[0].append(num)
         
        for num in nums2set:
            if num not in nums1set:
                res[1].append(num)
        return res