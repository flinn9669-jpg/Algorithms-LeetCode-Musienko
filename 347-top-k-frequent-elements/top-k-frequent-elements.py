class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #считает сколько раз встречается каждое число
        count = Counter(nums)
        #создаёт "карманы" по количеству повторений
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        result = []
        #идёт с конца 
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result