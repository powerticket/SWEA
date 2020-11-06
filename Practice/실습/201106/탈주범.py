from collections import deque
import sys
sys.stdin = open('sample_input.txt')


def check(r, c):
    up = down = left = right = 1
    if arr[r][c] == 2:
        left = right = 0
    elif arr[r][c] == 3:
        up = down = 0
    elif arr[r][c] == 4:
        left = down = 0
    elif arr[r][c] == 5:
        left = up = 0
    elif arr[r][c] == 6:
        up = right = 0
    elif arr[r][c] == 7:
        right = down = 0
    return (up, down, left, right)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    q = deque();
    q.append((R, C))
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    time = 1;
    while time < L:
        cycle = len(q)
        for _ in range(cycle):
            r, c = q.popleft()
            up, down, left, right = check(r, c)
            if r - 1 >= 0:
                if not visited[r-1][c] and up:
                    if check(r-1, c)[1]:
                        q.append((r-1, c))
                        visited[r-1][c] = 1
            if r + 1 < N:
                if not visited[r+1][c] and down:
                    if check(r+1, c)[0]:
                        q.append((r+1, c))
                        visited[r+1][c] = 1
            if c - 1 >= 0:
                if not visited[r][c-1] and left:
                    if check(r, c-1)[3]:
                        q.append((r, c-1))
                        visited[r][c-1] = 1
            if c + 1 < M:
                if not visited[r][c+1] and right:
                    if check(r, c+1)[2]:
                        q.append((r, c+1))
                        visited[r][c+1] = 1
        time += 1
    result = 0
    for i in range(N):
        result += sum(visited[i])
    print('#{} {}'.format(t, result))