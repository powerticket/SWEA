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
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        minr = minc = -1
        minV = INF
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    fuel = cost[r][c] + 1
                    diff = arr[nr][nc] - arr[r][c]
                    if diff > 0:
                        fuel += diff
                    if fuel < minV:
                        minV = fuel
                        minr, minc = nr, nc
        queue.append((minr, minc))
        visited[minr][minc] = 1
        cost[minr][minc] = minV
    result = cost[N-1][N-1]
    print('#{} {}'.format(t, result))
