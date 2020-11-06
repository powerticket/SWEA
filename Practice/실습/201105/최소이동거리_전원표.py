from collections import deque

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w
    INF = 0xffffffff
    cost = [INF] * (N+1)
    visited = [0] * (N+1)
    cost[0] = 0
    for _ in range(N+1):
        minV = INF
        minIdx = -1
        for i in range(N+1):
            if not visited[i] and cost[i] < minV:
                minV = cost[i]
                minIdx = i
        visited[minIdx] = 1
        for i in range(N+1):
            if G[minIdx][i] and not visited[i] and cost[minIdx] + G[minIdx][i] < cost[i]:
                cost[i] = cost[minIdx] + G[minIdx][i]
    print('#{} {}'.format(t, cost[N]))
