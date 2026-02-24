class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x*x + y*y  #квадрат расстояния до (0,0)           
            #кладёт точку в кучу
            heapq.heappush(heap, (dist, [x, y]))
        #берёт k ближайших
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result     