class Solution:
    def getLandNeighbors(self, grid, i, j):
        num_rows = len(grid)
        num_cols = len(grid[0])
        results = []
        if i != 0 and grid[i-1][j] == "1":
            results.append((i-1, j))
        if i != num_rows-1 and grid[i+1][j] == "1":
             results.append((i+1, j))
        if j != 0 and grid[i][j-1] == "1":
             results.append((i, j-1))
        if j != num_cols-1 and grid[i][j+1] == "1":
            results.append((i, j+1))
        return results

    def dfs(self, grid, i, j):
        for ni, nj in self.getLandNeighbors(grid, i, j):
            grid[ni][nj] = 0
            self.dfs(grid, ni, nj)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1
        
        return num_islands
