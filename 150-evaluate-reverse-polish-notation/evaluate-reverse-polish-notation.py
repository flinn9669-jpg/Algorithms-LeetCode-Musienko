class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            #если это оператор
            if token in "+-*/":
                b = stack.pop()  #второй операнд
                a = stack.pop()  #первый операнд   
                #выполняет операцию
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  #деление
                    #int() обрезает к нулю 
                    stack.append(int(a / b))
            else:
                #если число, то добавляет в стек
                stack.append(int(token))
        #в конце остаётся один элемент
        return stack[0]