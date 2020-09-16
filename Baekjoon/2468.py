import sys
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(sys.stdin.readline())
area = [[*map(int, sys.stdin.readline().split())] for _ in ' '*N]
max_height = max(map(max, area))
max_isolation = 1
q = deque()
for height in range(max_height):
    visited = [[0] * N for _ in ' '*N]
    isolation = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] - height > 0:
                isolation += 1
                visited[i][j] = 1
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if area[nr][nc] - height <= 0:
                                visited[nr][nc] = 1
                                continue
                            if not visited[nr][nc]:
                                visited[nr][nc] = 1
                                q.append((nr, nc))
    if isolation > max_isolation:
        max_isolation = isolation
print(max_isolation)
