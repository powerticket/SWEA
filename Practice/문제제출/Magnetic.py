import sys
sys.stdin = open('input.txt', 'r')


def check(r, c, p):
    if p == 1:
        if r == N-1:
            return 1
        if not L[r+1][c]:
            if check(r+1, c, p):
                return 1
    elif p == 2:
        if r == 0:
            return 1
        if not L[r-1][c]:
            if check(r-1, c, p):
                return 1
    return


for t in range(1, 11):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if L[i][j] == 2:
                if check(i, j, 2):
                    L[i][j] = 0
    for i in range(N-1, -1, -1):
        for j in range(N):
            if L[i][j] == 1:
                if check(i, j, 1):
                    L[i][j] = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if L[i][j] == 2:
                cnt += 1
    print('#{} {}'.format(t, cnt))