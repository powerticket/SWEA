dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(i, j):
    visited = [[0] * 16 for _ in range(16)]
    visited[i][j] = 1
    queue = [(i, j)]
    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if arr[nr][nc] == 3:
                    return 1
                elif not arr[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
    return 0
                

for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    result = 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                result = bfs(i, j)
                break
        else:
            continue
        break
    print('#{} {}'.format(t, result))
