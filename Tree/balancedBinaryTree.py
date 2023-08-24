class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None: return True
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1: return False
            return check(root.left) and check(root.right)
        def height(root):
            if root is None: return 0
            lHeight = 1 + height(root.left)
            rHeight = 1 + height(root.right)
            return max(lHeight, rHeight)
        return check(root)
