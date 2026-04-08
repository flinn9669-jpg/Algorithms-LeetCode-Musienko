class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0   
        #собирает все гнилые и считаем свежие
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1   
        minutes = 0   
        #BFS по уровням 
        while queue and fresh > 0:
            for _ in range(len(queue)):  #текущий "слой"
                r, c = queue.popleft()   
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc     
                    #если внутри и это свежий апельсин
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2     #делает гнилым
                        fresh -= 1           #уменьшает счётчик
                        queue.append((nr, nc))
            minutes += 1
        # если остались свежие, то невозможно
        return minutes if fresh == 0 else -1