class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):
            grid[r][c] = "0"
            stack = [(r, c)]
        
            while stack: 
                row, col = stack.pop()
                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    stack.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
        