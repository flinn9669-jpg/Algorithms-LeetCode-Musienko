class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums      
        #превращает список в минимальную кучу
        heapq.heapify(self.heap)
        #уменьшает кучу до размера k
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        #добавляет новый элемент
        heapq.heappush(self.heap, val)
        #если куча стала больше k - удаляет минимальный
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        #вершина кучи это k-й по величине
        return self.heap[0]