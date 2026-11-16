class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        stack = []
        res = 0
        
        def dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if not visit[nei]:
                        visit[nei] = True
                        stack.append(nei)
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res