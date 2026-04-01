class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #если дошел до пустого места, то вставляет новый узел
        if not root:
            return TreeNode(val)
        #идет влево или вправо в зависимости от значения
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val) 
        return root  #возвращает корень 