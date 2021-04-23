import sys
sys.stdin = open('0423_16236.txt', 'r')

# 04/23
# 16236 아기 상어
def eat(r, c):
    queue = [(r, c)]
    time = 0
    visited = [[0] * N for _ in range(N)]
    temp = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    stop = 0
    while queue:
        cycle = len(queue)
        for _ in range(cycle):
            r, c = queue.pop(0)
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= shark_lvl:
                    if 0 < arr[nr][nc] < shark_lvl:
                        stop = 1
                        temp[nr][nc] = 1
                    else:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
        time += 1
        if stop:
            for i in range(N):
                for j in range(N):
                    if temp[i][j]:
                        arr[i][j] = 0
                        return (i, j, time)
    return (-1, -1, -1)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            r, c = i, j
            arr[i][j] = 0
shark_lvl = 2
lvl_up = 0
result = 0
while 1:
    r, c, time = eat(r, c)
    if r == -1:
        break
    result += time
    lvl_up += 1
    if shark_lvl == lvl_up:
        shark_lvl += 1
        lvl_up = 0
print(result)
