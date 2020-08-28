"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c):
    arr[r][c] = 2
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 0 or arr[nr][nc] == 2:
            continue
        dfs(nr, nc)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
for row in arr:
    print(row)
print("---")
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            dfs(i, j)
for row in arr:
    print(row)
