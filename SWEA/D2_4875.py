def go_maze(r, c):
    if maze[r][c] == 3:
        return 1
    elif maze[r][c] == 0:
        maze[r][c] = 4
        if r < N-1:
            if go_maze(r+1, c):
                return 1
        if r > 0:
            if go_maze(r-1, c):
                return 1
        if c < N-1:
            if go_maze(r, c+1):
                return 1
        if c > 0:
            if go_maze(r, c-1):
                return 1
        maze[r][c] = 5
    return 0

        

for t in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sr, sc = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
    maze[sr][sc] = 0
    print('#{} {}'.format(t, go_maze(sr, sc)))
