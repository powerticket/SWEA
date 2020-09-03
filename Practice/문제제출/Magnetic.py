import sys
sys.stdin = open('input.txt', 'r')


def move(r, c, p):
    L[r][c] = p
    if p == 1:
        if r == N-1:
            L[r][c] = 0
            return
        if not L[r+1][c]:
            L[r][c] = 0
            move(r+1, c, p)
    elif p == 2:
        if r == 0:
            L[r][c] = 0
            return
        if not L[r-1][c]:
            L[r][c] = 0
            move(r-1, c, p)


for t in range(1, 11):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if L[i][j]:
                move(i, j, L[i][j])

    result = 0
    for i in range(N):
        for j in range(1, N):
            if L[j-1][i] == 1 and L[j][i] == 2:
                result += 1

    print('#{} {}'.format(t, result))
