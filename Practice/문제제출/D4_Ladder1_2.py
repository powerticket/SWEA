import sys
sys.stdin = open('input.txt', 'r')


def search(r, c):
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    num = ladder[r][c]
    visited = [[0] * 100 for _ in range(100)]
    visited[r][c] = 1

    while 1:
        if num == 2:
            return True

        if r == 99:
            return False

        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= 100 or nc < 0 or nc >= 100:
                continue
            if ladder[nr][nc] == 0:
                continue
            if visited[nr][nc] == 1:
                continue
            r = nr
            c = nc
            num = ladder[nr][nc]
            visited[nr][nc] = 1
            break


for _ in range(1, 11):
    t = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[0][i]:
            result = search(0, i)
        if result:
            cnt = i
            break
    print('#{} {}'.format(t, cnt))