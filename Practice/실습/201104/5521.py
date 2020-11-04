T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    rel = [list(map(int, input().split())) for _ in range(M)]
    G = [[0] * (N+1) for _ in range(N+1)]
    for s, e in rel:
        G[s][e] = G[e][s] = 1
    result = 0
    queue = []
    visited = [0] * (N+1)
    queue.append(1)
    visited[1] = 1
    while queue:
        v = queue.pop(0)
        if visited[v] > 3:
            break
        for w in range(N+1):
            if G[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1
                if visited[w] < 4:
                    result += 1
    print('#{} {}'.format(t, result))
