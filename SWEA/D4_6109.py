import sys
sys.stdin = open('s_input.txt', 'r')


def rm_bubble(L, N, D):
    dr, dc, dstart, dend, cstart, cend = direction(N, D)
    for i in range(N-dstart, N-dend, -dr):
        for j in range(N-cstart, N-cend, -dc):
            if L[i-dr][j-dc] == 0:
                L[i-dr][j-dc] = L[i][j]
                L[i][j] = 0
    return L


def move(L, N, D):
    dr, dc, dstart, dend, cstart, cend = direction(N, D)
    for i in range(dstart, dend):
        for j in range(cstart, cend):
            if L[i][j] == L[i+dr][j+dc]:
                L[i][j] *= 2
                L[i+dr][j+dc] = 0
    return L


def direction(N, D):
    dr, dc, dstart, dend, cstart, cend = 0, 0, 1, N, 1, N
    if D == 'up':
        dr = 1
        dstart, dend = 1, N
    elif D == 'down':
        dr = -1
        dstart, dend = N-1, 0
    elif D == 'left':
        dc = 1
        cstart, cend = 1, N
    else:
        dc = -1
        cstart, cend = N-1, 0
    return dr, dc, dstart, dend, cstart, cend


for t in range(1, int(input())+1):
    N, D = input().split()
    N = int(N)
    L = [list(map(int, input().split())) for _ in range(N)]
    L = rm_bubble(L, N, D)
    # move()
    # rm_bubble()
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(L[i][j], end=' ')
        print()
