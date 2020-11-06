from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 0xffffffff
    cost = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cost[0][0] = 0
    for _ in range(N*N):
        minV = INF
        minr = minc = -1
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and cost[i][j] < minV:
                    minV = cost[i][j]
                    minr, minc = i, j
        visited[minr][minc] = 1
        for d in range(4):
            nr = minr + dr[d]
            nc = minc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    diff = arr[nr][nc] - arr[minr][minc]
                    if diff < 0:
                        diff = 0
                    cost[nr][nc] = min(cost[nr][nc], cost[minr][minc] + diff + 1)
    result = cost[N-1][N-1]
    print('#{} {}'.format(t, result))
