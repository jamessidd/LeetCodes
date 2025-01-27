class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                left = flowerbed[i - 1] if i > 0 else 0
                right = flowerbed[i + 1] if i < (len(flowerbed) - 1) else 0

                if left == 0 and right == 0:
                    flowerbed[i] = 1
                    # print(flowerbed)
                    n -= 1

                    if n == 0:
                        return True
            i += 1
        if n > 0:
            return False
        else:
            return True

        