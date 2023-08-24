from typing import List
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        bfs = []
        visited = {}
        queue = [0]
        visited[0] = True
        while (queue):
            node = queue.pop(0)
            bfs.append(node)
            for nei in adj[node]:
                if (nei not in visited):
                    visited[nei] = True
                    queue.append(nei)
        return bfs
