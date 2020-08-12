class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        area_list = [] #list of the area of islands
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area_list.append(0)
                    self.dfs(i, j, grid, area_list)
        
        if area_list:
            max_area = max(area_list)

        return max_area
        
    def dfs(self, i, j, grid, area_list):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = -1
            area_list[-1] += 1
            self.dfs(i-1, j, grid, area_list)
            self.dfs(i+1, j, grid, area_list)
            self.dfs(i, j-1, grid, area_list)
            self.dfs(i, j+1, grid, area_list)
        else:
            return