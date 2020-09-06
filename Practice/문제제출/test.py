def bfs(x, y):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    q = []
    visited = []
    q.append([x, y])
    visited.append([x, y])
    distance = [[0] * N for _ in range(N)]
    while len(q) != 0:
        n = q.pop(0)
        for i in range(4):
            nr = n[0] + dr[i]
            nc = n[1] + dc[i]
            if 0 <= nr < N and 0 <= nc <N and [nr, nc] not in visited:
                if arr[nr][nc] == 3:
                    return distance[n[0]][n[1]]
                elif arr[nr][nc] == 0:
                    q.append([nr, nc])
                    visited.append([nr, nc])
                    arr[nr][nc] = 1
                    distance[nr][nc] = distance[n[0]][n[1]] + 1
    return 0

for t in range(1, int(input())+1):
    N = int(input())
    arr = [[int(k) for k in input()] for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            x, y = i, j
            break
result = bfs(x,y)
print("#{} {}".format(t, result))