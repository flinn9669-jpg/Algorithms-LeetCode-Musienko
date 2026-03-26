class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)  #добавляет (но порядок будет обратный)          
            #сначала кладет левого, потом правого
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)       
        #переворачивает результат и получает postorder
        return result[::-1]