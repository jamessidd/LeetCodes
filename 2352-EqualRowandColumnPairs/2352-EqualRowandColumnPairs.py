class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rdict = defaultdict(list)
        cdict = defaultdict(list)

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                rdict[row].append(grid[row][col])
                cdict[col].append(grid[row][col])
        count = 0
        for rows in rdict.values():

            for cols in cdict.values():

                if rows == cols:
                    count +=1
        
        return count

            