class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #если длины разные, то сразу не анаграммы
        if len(s) != len(t):
            return False
        count = {}  #хэш-таблица
        #считает символы из строки s
        for char in s:
            count[char] = count.get(char, 0) + 1
        #вычитает символы из строки t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
        #проверяет, что все значения равны 0
        for value in count.values():
            if value != 0:
                return False
        return True