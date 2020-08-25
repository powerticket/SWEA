import sys
sys.stdin = open('input.txt', 'r')


def palin(i, j):
    cnt_list = []
    cnt = 0
    d = 0
    while j-d >= 0 and j+d+1 < 100 and L[i][j-d] == L[i][j+d+1]:
        d += 1
        cnt += 2
    cnt_list.append(cnt)
    cnt = 1
    d = 0
    while j-d-1 >= 0 and j+d+1 < 100 and L[i][j-d-1] == L[i][j+d+1]:
        d += 1
        cnt += 2
    cnt_list.append(cnt)
    cnt = 0
    d = 0
    while i-d >= 0 and i+d+1 < 100 and L[i-d][j] == L[i+d+1][j]:
        d += 1
        cnt += 2
    cnt_list.append(cnt)
    cnt = 1
    d = 0
    while i-d-1 >= 0 and i+d+1 < 100 and L[i-d-1][j] == L[i+d+1][j]:
        d += 1
        cnt += 2
    cnt_list.append(cnt)
    return max(cnt_list)


for _ in range(1, 11):
    t = int(input())
    L = [input() for _ in range(100)]
    result = []
    for i in range(99):
        for j in range(99):
            result.append(palin(i, j))
    print('#{} {}'.format(t, max(result)))