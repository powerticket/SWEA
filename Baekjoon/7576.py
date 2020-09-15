import sys
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

if all(map(all, tomato)):
    print(0)
else:
    q = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1
    result = 0
    while q:
        r, c = q.popleft()
        result = visited[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc] or tomato[nr][nc] == -1:
                continue
            if not tomato[nr][nc]:
                visited[nr][nc] += visited[r][c] + 1
                tomato[nr][nc] = 1
                q.append((nr, nc))

    if all(map(all, tomato)):
        print(result-1)
    else:
        print(-1)
