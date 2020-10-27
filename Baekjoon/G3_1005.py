T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    relation = [list(map(int, input().split())) for _ in range(K)]
    W = int(input())
    G = [[] for _ in range(N+1)]
    for start, end in relation:
        G[end].append(start)
    visited = [0] * (N+1)
    q = [W]
    visited[W] = D[W]
    while q:
        v = q.pop(0)
        for w in G[v]:
            q.append(w)
            visited[w] = max(visited[w], visited[v] + D[w])
    print(max(visited))
