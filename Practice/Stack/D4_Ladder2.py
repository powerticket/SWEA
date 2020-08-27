import sys
sys.stdin = open('input.txt', 'r')


def dfs(c):
    v = [0] * 100
    s = []
    r = 0
    s.append(c)
    v[c] = 1
    cnt = 0

    while s:
        cnt += 1
        c = s.pop()
        if c-1 >= 0 and L[r][c-1] and not v[c-1]:
            v[c-1] = 1
            s.append(c-1)
        elif c+1 < 100 and L[r][c+1] and not v[c+1]:
            v[c+1] = 1
            s.append(c+1)
        elif r < 99:
            v = [0] * 100
            v[c] = 1
            s.append(c)
            r += 1
        else:
            return cnt
    return 10000



for _ in range(1, 11):
    t = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10000
    min_x = 0
    for i in range(100):
        if L[0][i]:
            cnt = dfs(i)
            if cnt < min_cnt:
                min_cnt = cnt
                min_x = i
    print('#{} {}'.format(t, min_x))
