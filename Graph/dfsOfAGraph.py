class Solution:    
    def dfsOfGraph(self, V, adj):
        def dfs(node):
            visited[node] = True
            arr.append(node)
            for nei in adj[node]:
                if (nei not in visited):
                    dfs(nei)
        visited = {}
        visited[0] = True
        arr = []
        dfs(0)
        return arr
