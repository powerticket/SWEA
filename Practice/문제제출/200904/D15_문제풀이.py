dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    Q = []
    Q.append((r, c))
    visited[r][c] = 1
    while Q:        
        r, c = Q.pop(0)
        if visited[r][c] == 7:
            break
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                continue
            Q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
    return visited


for t in range(1, int(input())+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    cnt = 0
    for i in range(4):
        for j in range(4):
            visited = [[0] * 4 for _ in range(4)]
            bfs(i, j)
            for row in visited:
                print(row)
            print('-----------')
    # print('#{} {}'.format(t, len(result)))
