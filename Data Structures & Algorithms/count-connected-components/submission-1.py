class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)   
        res = 0

        def bfs(node):
            q = deque([node])
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                bfs(node)
                res += 1
        return res