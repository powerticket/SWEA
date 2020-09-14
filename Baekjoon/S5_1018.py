'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
'''
def check(r, c, color):
    global cnt
    visited[r][c] = 1
    if color != board[r][c]:
        cnt += 1
    if color == 'W':
        color = 'B'
    else:
        color = 'W'
    if r < N-1 and not visited[r+1][c]:
        check(r+1, c, color)
    if c < M-1 and not visited[r][c+1]:
        check(r, c+1, color)

N, M = map(int, input().split())
board = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
check(0, 0, 'W')
print(cnt)