class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  #стек для хранения открывающих скобок
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            #если это открывающая скобка, то кладёт в стек
            if char in '([{':
                stack.append(char)
            else:
                #если стек пуст или не совпадает тип, то ошибка
                if not stack or stack[-1] != mapping[char]:
                    return False        
                #если всё ок, то убирает последнюю открывающую
                stack.pop()
        #если стек пуст, то всё корректно
        return len(stack) == 0