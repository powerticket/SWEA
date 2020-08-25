def direction(D):
    d, dr, dc, rstart, rend, cstart, cend = 1, 0, 0, 0, 0, 0, 0
    if D == 'up':
        rstart, rend, cstart, cend = 0, N-1, 0, N
        dr = -1
    elif D == 'down':
        dr = 1
        rstart, rend, cstart, cend = N-1, 0, 0, N
        d= -1
    elif D == 'left':
        dc = -1
        rstart, rend, cstart, cend = 0, N, 0, N-1
    else:
        dc = 1
        rstart, rend, cstart, cend = 0, N, N-1, 0
        d = -1
    return d, dr, dc, rstart, rend, cstart, cend


def bubble_pop(L, D):
    d, dr, dc, rstart, rend, cstart, cend = direction(D)
    for i in range(rstart, rend, d):
        for j in range(cstart, cend, d):
            if L[i][j] == 0:
                L[i][j] = L[i-dr][j-dc]
                L[i-dr][j-dc] = 0
    return L


def move(L, D):
    d, dr, dc, rstart, rend, cstart, cend = direction(D)
    for i in range(rstart, rend, d):
        for j in range(cstart, cend, d):
            if L[i-dr][j-dc] == L[i][j]:
                L[i][j] *= 2
                L[i-dr][j-dc] = 0
    return L


for t in range(1, int(input())+1):
    N, D = input().split()
    N = int(N)
    L = [list(map(int, input().split())) for _ in range(N)]
    L = bubble_pop(move(bubble_pop(L, D), D), D)
    for i in range(N):
        for j in range(N):
            print(L[i][j], end=' ')
        print()
'''
1
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
'''