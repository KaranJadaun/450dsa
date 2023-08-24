class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def solve(root):
            if root is None: return 0
            left = solve(root.left)
            right = solve(root.right)
            self.maxi = max(self.maxi, left + right)
            return max(left, right) + 1 
        solve(root)
        return self.maxi 
