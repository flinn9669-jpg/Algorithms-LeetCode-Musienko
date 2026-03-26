class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []   #код будет записывать ответ
        stack = []    #стек для обхода
        current = root
        #пока есть узлы для обработки
        while current or stack:
            #идет максимально влево
            while current:
                stack.append(current)
                current = current.left
            #достает узел из стека
            current = stack.pop()
            result.append(current.val)  #обрабатывает узел
            #переходит к правому поддереву
            current = current.right
        return result     