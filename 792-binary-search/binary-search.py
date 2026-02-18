class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left начало 
        #right конец 
        left, right = 0, len(nums) - 1
        #пока левая граница не пересекла правую
        while left <= right:
            #находит середину текущего диапазона
            mid = (left + right) // 2
            #если элемент в середине это то что надо 
            if nums[mid] == target:
                return mid  #возвращает его индекс
            #если искомое число больше, чем число в середине
            elif nums[mid] < target:
                left = mid + 1  #сдвигает левую границу вправо
            #если число меньше, ищет слева
            else:
                right = mid - 1  #сдвигает правую границу влево
        #если число не найдено, возвращает -1
        return -1