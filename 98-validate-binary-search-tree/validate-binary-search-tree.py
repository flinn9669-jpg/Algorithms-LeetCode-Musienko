class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:      
        def helper(node, low, high):
            if not node:
                return True       
            #проверяет, входит ли значение в допустимый диапазон
            if not (low < node.val < high):
                return False  
            #проверяет левое и правое поддерево
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        #стартует с бесконечными границами
        return helper(root, float('-inf'), float('inf'))