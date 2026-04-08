class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        #строит граф
        for u, v, w in times:
            graph[u].append((v, w))
        #минимальные расстояния
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        #(время, вершина)
        heap = [(0, k)] 
        while heap:
            time, node = heapq.heappop(heap)     
            #если нашел лучше раньше, то пропускает
            if time > dist[node]:
                continue
            for nei, w in graph[node]:
                new_time = time + w   
                #обновляет расстояние
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))
        #берёт максимум времени
        max_time = max(dist.values())
        return max_time if max_time != float('inf') else -1