class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None      
        #ищет нужный узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #нашел узел
            #если нет левого ребенка
            if not root.left:
                return root.right
            #если нет правого ребенка
            if not root.right:
                return root.left
            #если есть оба ребенка
            #ищет минимум в правом поддереве
            min_node = self.getMin(root.right)
            #заменяет значение
            root.val = min_node.val
            #удаляет этот минимум
            root.right = self.deleteNode(root.right, min_node.val)
        return root
    #вспомогательная функция, ищет минимум
    def getMin(self, node):
        while node.left:
            node = node.left
        return node