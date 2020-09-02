import sys
sys.stdin = open('input.txt', 'r')


def check(L, i):
    c = 0
    cnt = 0
    for j in range(N):
        if L[i][j]:
            cnt += 1
        if not L[i][j] or j == N-1:
            if cnt == K:
                c += 1
            cnt = 0
    return c


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    box_rev = list(zip(*box))
    total = 0
    for i in range(N):
        total += check(box, i)
        total += check(box_rev, i)

    print('#{} {}'.format(t, total))
