def bfs(G, v):
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)
        for w in G[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1


