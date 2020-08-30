dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def check(r, c, s):
    result = []
    for d in range(8):
        nr = r
        nc = c
        while 1:
            nr += dr[d]
            nc += dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or not B[nr][nc]:
                break
            if B[nr][nc] == s:
                result.append(d)
                break
    return result


def oth(r, c, s, d):
    while 1:
        r += dr[d]
        c += dc[d]
        if r < 0 or r >= N or c < 0 or c >= N:
            break
        if B[r][c] == s or not B[r][c]:
            break
        B[r][c] = s


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    B = [[0] * N for _ in range(N)]
    B[N//2-1][N//2], B[N//2][N//2-1] = 1, 1
    B[N//2-1][N//2-1], B[N//2][N//2] = 2, 2
    for r, c, s in arr:
        r -= 1
        c -= 1
        B[r][c] = s
        for d in check(r, c, s):
            oth(r, c, s, d)
    result = [0, 0]
    for i in range(N):
        for j in range(N):
            if B[i][j] == 1:
                result[0] += 1
            elif B[i][j] == 2:
                result[1] += 1
    print('#{} {} {}'.format(t, result[0], result[1]))