class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  #быстро отсекает разные длины
        count = defaultdict(int)  #словарь
        #считает буквы в s
        for char in s:
            count[char] += 1
        #вычитает буквы из t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True  #все буквы совпали