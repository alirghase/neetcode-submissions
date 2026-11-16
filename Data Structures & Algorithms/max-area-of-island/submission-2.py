class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs
        rows, cols = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            stack = [(r, c)]
            area = 0
            grid[r][c] = 0

            while stack:
                row, col = stack.pop()
                area += 1
                for dr, dc in directions: 
                    nr, nc = row + dr, col + dc 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        stack.append([nr, nc])
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area
