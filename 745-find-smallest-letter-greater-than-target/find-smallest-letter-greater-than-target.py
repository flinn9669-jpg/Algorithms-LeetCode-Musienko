class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1       
        while left <= right:
            #находит середину
            mid = (left + right) // 2           
            #если буква в середине меньше или равна target, значит нужная буква правее
            if letters[mid] <= target:
                left = mid + 1
            #иначе нужная буква левее
            else:
                right = mid - 1
        #после выхода из цикла left указывает на первую букву, которая больше target
        #если вышел за границы массива, то возвращает первую букву 
        return letters[left] if left < len(letters) else letters[0]