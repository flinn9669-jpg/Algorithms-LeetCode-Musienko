class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []      
        result = []   #список для результата
        stack = [root]  #начинает с корня      
        while stack:
            node = stack.pop()  #достает текущий узел
            result.append(node.val)  #обрабатывает         
            #сначала кладет правого, потом левого
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)       
        return result       