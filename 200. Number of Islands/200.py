# 深度优先搜索，迭代思想

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        count = 0
        def DFS(grid, i, j):
            
            if i + 1 < row and grid[i+1][j] == '1': 
                grid[i+1][j] = 'X'
                DFS(grid, i+1, j)
            if j + 1 < col and grid[i][j+1] == '1':
                grid[i][j+1] = 'X'
                DFS(grid, i, j+1)
            if i - 1 >= 0 and grid[i-1][j] == '1':
                grid[i-1][j] = 'X'
                DFS(grid, i-1, j)
            if j - 1 >= 0 and grid[i][j-1] == '1':
                grid[i][j-1] = 'X'
                DFS(grid, i, j-1)
                
                
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    grid[i][j] = 'X'
                    DFS(grid, i, j)
                    count += 1
        
        return count