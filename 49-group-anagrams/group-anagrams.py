class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}  
        for word in strs:
            #сортирует строку, чтобы получить ключ
            key = ''.join(sorted(word))
            #если ключа нет, то создаёт список
            if key not in anagrams:
                anagrams[key] = []
            #добавляет слово в группу
            anagrams[key].append(word)
        #возвращает только группы
        return list(anagrams.values())     