class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  #использует set как хэш-таблицу
        for num in nums:
            #если элемент уже встречался, значит есть дубликат
            if num in seen:
                return True
            #добавляет элемент в множество
            seen.add(num)
        return False  #если дубликатов нет     