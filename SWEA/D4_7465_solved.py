T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    relation = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    result = 0
    # 인접 리스트
    for i in range(M):
        s, e = relation[i][0], relation[i][1]
        G[s].append(e)
        G[e].append(s)
    # bfs 탐색 및 무리 카운트
    for i in range(1, N+1):
        if not visited[i]:
            result += 1
            queue = []
            queue.append(i)
            visited[i] = 1
            while queue:
                v = queue.pop(0)
                for w in G[v]:
                    if not visited[w]:
                        queue.append(w)
                        visited[w] = 1
    print('#{} {}'.format(t, result))