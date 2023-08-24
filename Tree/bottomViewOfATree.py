class Solution:
    def bottomView(self, root):
        hashmap = {}
        queue = [(root, 0)]
        while (queue):
            root, level = queue.pop(0)
            if (level not in hashmap):
                hashmap[level] = root.data
            else:
                hashmap[level] = root.data
            if (root.left): queue.append((root.left, level - 1))
            if (root.right): queue.append((root.right, level + 1))
        arr = []
        for i in sorted(hashmap.keys()):
            arr.append(hashmap[i])
        return arr    
            
