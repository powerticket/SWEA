def bfs(v):
    visited = [0] * (V+1)
    Q = []
    Q.append((v))
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if G[v][w] and not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1


V, E = 7, 8
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    s, e = temp[2 * i], temp[2 * i + 1]
    G[s][e] = G[e][s] = 1

for i in range(1, V+1):
    print(G[i])
