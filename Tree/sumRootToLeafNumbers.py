class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def path(root, s):
            if root is None:
                return
            s += str(root.val)
            if root.left is None and root.right is None:
                arr.append(s)
                return
            left = path(root.left, s)
            right = path(root.right, s)
        path(root, "")
        s = 0
        for i in arr:
            s += int(i)
        return s
