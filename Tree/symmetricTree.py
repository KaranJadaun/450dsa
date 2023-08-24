class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def solve(root1, root2):
            if self.ans == False: return 
            if root1 is None and root2 is None:
                return
            if root1 is None or root2 is None:
                self.ans = False
                return
            if root1.val != root2.val:
                self.ans = False
            solve(root1.left, root2.right)
            solve(root1.right, root2.left)
        solve(root.left, root.right)
        return self.ans
