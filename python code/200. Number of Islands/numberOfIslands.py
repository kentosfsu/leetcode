class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """       
        island_count = 0
        
        def search_adjacent_lands(i, j, grid):
            # print(i, j)
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == "0" or grid[i][j] == "-1":
                return
            elif grid[i][j] == "1":
                grid[i][j] = "-1" #mark as visited
                search_adjacent_lands(i-1, j, grid)
                search_adjacent_lands(i+1, j, grid)
                search_adjacent_lands(i, j-1, grid)
                search_adjacent_lands(i, j+1, grid)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_count += 1
                    search_adjacent_lands(i, j, grid)
        return island_count