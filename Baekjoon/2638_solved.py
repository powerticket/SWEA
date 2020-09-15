import sys


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

while sum(map(sum, cheese)):
    air = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = []
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if cheese[nr][nc]:
                air[nr][nc] += 1
                continue
            if not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    for i in range(1, N-1):
        for j in range(1, M-1):
            if air[i][j] > 1:
                cheese[i][j] = 0
    result += 1
print(result)

'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
'''