class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None
        def preorder(root):
            if root is None: return None
            preorder(root.right)
            preorder(root.left)
            root.left = None
            root.right = self.prev
            self.prev = root
        preorder(root)
        return root
