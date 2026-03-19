class Solution:
    def twoSum(self, nums, target):
        hmap = {} 
        for i, num in enumerate(nums):
            complement = target - num  #число, которое нужно найти  
            #если нужное число уже есть в словаре    
            if complement in hmap:
                return [hmap[complement], i] 
            #добавляет текущее число в словарь        
            hmap[num] = i
        return []