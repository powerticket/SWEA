from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 0xffffffff
    q = deque()
    cost = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q.append((0, 0))
    cost[0][0] = 0
    while q:
        r, c = q.popleft()
        visited[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                diff = arr[nr][nc] - arr[r][c]
                if diff < 0:
                    diff = 0
                fuel = cost[r][c] + 1 + diff
                if cost[nr][nc] > fuel:
                    cost[nr][nc] = fuel                    
                    q.append((nr, nc))
    print('#{} {}'.format(t, cost[N-1][N-1]))
