class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #основная функция сортировки слиянием
        def merge_sort(arr):
            #если массив пустой или содержит один элемент, то он уже отсортирован
            if len(arr) <= 1:
                return arr
            #находит середину массива
            mid = len(arr) // 2
            #рекурсивно сортирует левую и правую половины
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])  
            #объединяет две отсортированные половины в один массив
            return merge(left, right)
        #функция слияния двух отсортированных массивов
        def merge(left, right):
            i = j = 0  #указатели для левой и правой половины
            result = []  #складывает отсортированные элементы, пока есть элементы и в левом, и в правом массиве
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])  #добавляет меньший элемент
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            #добавляет оставшиеся элементы 
            result.extend(left[i:])
            result.extend(right[j:])           
            return result  #возвращает объединённый отсортированный массив
        #запускает сортировку слиянием для всего исходного массива
        return merge_sort(nums)