# beat 100%
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # find how many lands adjacent to land grid[i][j]
                    # If a land exist more adjacent lands, less perimeter will add to the result
                    # Example: If one land has two adjacent lands, there will be only two edges of this land which can be considered to a effective egde for perimeter. If all of one land's adjacent grid are lands, this land can not provide contribution to the perimeter. 
                    perimeter += 4
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        perimeter -= 1
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        perimeter -= 1
                    if i+1 < row and grid[i+1][j] == 1:
                        perimeter -= 1
                    if j+1 < col and grid[i][j+1] == 1:
                        perimeter -= 1
        return perimeter