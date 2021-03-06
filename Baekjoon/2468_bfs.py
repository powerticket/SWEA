from sys import stdin


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]


N = int(stdin.readline())
L = [list(map(int, stdin.readline().split())) for _ in range(N)]
MAX = max(map(max, L))
max_result = 1
for h in range(1, MAX):
    visited = [[0] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and L[i][j] > h:
                q = []
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    r, c = q.pop(0)
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        if visited[nr][nc] or L[nr][nc] <= h:
                            continue
                        q.append((nr, nc))
                        visited[nr][nc] = 1
                result += 1
    if result > max_result:
        max_result = result
print(max_result)