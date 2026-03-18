class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k   #массив фиксированного размера
        self.k = k             #размер очереди
        self.front = 0         #указатель на начало
        self.rear = 0          #указатель на следующий свободный слот
        self.count = 0         #количество элементов в очереди
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k  #двигает rear циклически
        self.count += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  #двигает front циклически
        self.count -= 1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        #rear указывает на следующий пустой слот, поэтому элемент перед ним
        return self.queue[(self.rear - 1 + self.k) % self.k]
    def isEmpty(self) -> bool:
        return self.count == 0
    def isFull(self) -> bool:
        return self.count == self.k