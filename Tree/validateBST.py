class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root, mini, maxi):
            if root is None: return True
            if root.val <= mini or root.val >= maxi: return False
            return inorder(root.left, mini, root.val) and inorder(root.right, root.val, maxi)
        return inorder(root, float('inf') * -1, float('inf'))
