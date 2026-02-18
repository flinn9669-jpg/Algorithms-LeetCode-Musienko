class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1               
        #пока левая граница не пересекла правую
        while left <= right:
            #находит середину текущего диапазона
            mid = (left + right) // 2                        
            #если он нашел нужное число то возвращает его индекс
            if nums[mid] == target:
                return mid            
            #если число в середине меньше нужного, то target правее
            elif nums[mid] < target:
                left = mid + 1            
            #если число в середине больше нужного, то target левее
            else:
                right = mid - 1               
        #если число не найдено, left будет указывать на место, куда его нужно вставить
        return left