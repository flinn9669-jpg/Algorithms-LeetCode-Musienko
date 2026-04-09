class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)    
        #минимальная стоимость подключения каждой точки
        min_dist = [float('inf')] * n    
        #отмечает, какие точки уже включены в MST
        used = [False] * n 
        #начинает с первой точки
        min_dist[0] = 0 
        result = 0 
        for _ in range(n):
            #находит точку с минимальной стоимостью
            u = -1
            for i in range(n):
                if not used[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i 
            #добавляет её в MST
            used[u] = True
            result += min_dist[u] 
            #обновляет расстояния до остальных точек
            for v in range(n):
                if not used[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist
        return result