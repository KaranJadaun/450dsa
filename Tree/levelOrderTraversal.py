class Solution:
    def levelOrder(self, root):
        ans = []
        if (root is None): return ans
        queue = []
        queue.append(root)
        while (queue):
            n = len(queue)
            level = []
            for _ in range(n):
                root = queue.pop(0)
                if (root.left is not None):
                    queue.append(root.left)
                if (root.right is not None):
                    queue.append(root.right)
                level.append(root.val)
            ans.append(level)
        return ans
