# Time Complexity: row * columns --> from the loop
# Space Complexity: row * column?
class Solution:
    def numIslands(self, grid):
        if grid == None or len(grid) == 0:
            return 0
        row = len(grid)
        column = len(grid[0])
        numberOfIslands = 0

        # navigate through each row
        for i in range(row):
            # navigate through columns
            for j in range(column):
                if grid[i][j] == "1":
                    numberOfIslands += self.dfs(grid, row, column, i, j)
        return numberOfIslands

    def dfs(self, grid, row, column, i, j):
        # check boundary
        # check if it's 0 or already visited
        if i < 0 or i >= row or j < 0 or j >= column or grid[i][j] != "1":
            return 0
        # mark as visited
        grid[i][j] = 2
        # check all the neighbors
        self.dfs(grid, row, column, i+1, j)
        self.dfs(grid, row, column, i-1, j)
        self.dfs(grid, row, column, i, j+1)
        self.dfs(grid, row, column, i, j-1)
        return 1
        
solution = Solution()
grid = [["0","1","0"],["1","0","1"],["0","1","0"]]
print(solution.numIslands(grid))