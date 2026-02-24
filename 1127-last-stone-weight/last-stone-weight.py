class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #делает максимальную кучу через отрицательные числа
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            #берёт два самых тяжёлых камня
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first != second:
                #разница возвращается в кучу
                heapq.heappush(max_heap, -(first - second))
        return -max_heap[0] if max_heap else 0