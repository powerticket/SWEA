import sys
sys.stdin = open('sample_input.txt', 'r')


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    stack = []
    stack.append((r, c))
    visited[r][c] = 1
    while stack:
        r, c = stack.pop(0)
        cnt = visited[r][c]
        if maze[r][c] == 3:
            return cnt - 2
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or maze[nr][nc] == 1:
                continue
            if not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1 + cnt
    return 0


for t in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = bfs(i, j)
                break
        else:
            continue
        break
    print('#{} {}'.format(t, result))