import sys
sys.stdin = open('input.txt', 'r')


def dfs(i):
    s = []
    r = 0
    s.append(i)
    visited = [0] * 100
    visited[i] = 1
    while s:
        n = s.pop()
        if n > 0 and L[r][n-1] and not visited[n-1]:
            s.append(n-1)
            visited[n-1] = 1
        elif n < 99 and L[r][n+1] and not visited[n+1]:
            s.append(n+1)
            visited[n+1] = 1
        else:
            r += 1
            if r == 99:
                if L[r][n] == 2:
                    return 1
                else:
                    return 0
            visited = [0] * 100
            s.append(n)
            visited[n] = 1


for _ in range(1, 11):
    t = input()
    L = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if L[0][i]:
            if dfs(i):
                print('#{} {}'.format(t, i))