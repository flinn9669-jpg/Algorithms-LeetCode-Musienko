class MyQueue:
    def __init__(self):
        self.in_stack = []   #стек для добавления элементов
        self.out_stack = []  #стек для удаления/чтения элементов
    def push(self, x: int) -> None:
        self.in_stack.append(x)  #просто добавляет в in_stack
    def pop(self) -> int:
        self.move_in_to_out()    #переносит элементы если нужно
        return self.out_stack.pop()
    def peek(self) -> int:
        self.move_in_to_out()    #переносит элементы если нужно
        return self.out_stack[-1]
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack  #очередь пустая, если оба стека пусты
    #вспомогательная функция: переносит элементы из in_stack в out_stack
    def move_in_to_out(self):
        if not self.out_stack:  #только если out_stack пуст
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())