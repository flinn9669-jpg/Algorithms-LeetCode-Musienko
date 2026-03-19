class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #преобразует списки в множества 
        set1 = set(nums1)
        set2 = set(nums2)
        #находит пересечение множеств
        result = set1 & set2
        return list(result)      