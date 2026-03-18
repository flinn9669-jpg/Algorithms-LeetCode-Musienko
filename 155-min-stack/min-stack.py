class MinStack:
    def __init__(self):
        self.stack = []      #основной стек
        self.min_stack = []  #стек минимумов
    def push(self, val: int) -> None:
        self.stack.append(val)   
        #если стек минимумов пуст или новый элемент меньше текущего минимума
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            #дублирует текущий минимум
            self.min_stack.append(self.min_stack[-1])
    def pop(self) -> None:
        self.stack.pop()       #удаляет из основного стека
        self.min_stack.pop()   #удаляет из стека минимумов
    def top(self) -> int:
        return self.stack[-1]  #возвращает верхний элемент
    def getMin(self) -> int:
        return self.min_stack[-1]  #минимум всегда сверху