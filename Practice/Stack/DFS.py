def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


N, E = 7, 8
# N, E = map(int, input().split())
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# temp = list(map(int, input().split()))
G = [[0] * (N+1) for _ in range(N+1)]
arr = [[0] * N for _ in range(N)]
visited = [0] * (N+1)
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e], G[e][s] = 1, 1

dfs(1)
