from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #делает минимальную кучу из первых k элементов
        heap = nums[:k]
        heapq.heapify(heap)
        #проходит по остальным элементам
        for num in nums[k:]:
            #если элемент больше минимального в куче
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        #вершина кучи - k-й по величине
        return heap[0]