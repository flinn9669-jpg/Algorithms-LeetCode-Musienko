class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0      
        rows, cols = len(grid), len(grid[0])
        count = 0       
        def dfs(r, c):
            #если выход за границы или вода, то стоп
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return          
            #убирает клетку, чтобы не считать повторно
            grid[r][c] = '0'           
            #идёт в 4 направления
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)       
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1          #нашел новый остров
                    dfs(i, j)           #убирает весь остров       
        return count        