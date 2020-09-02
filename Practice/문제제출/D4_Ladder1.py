import sys
sys.stdin = open('input.txt', 'r')


def dfs(c):
    visited = [0] * 101
    stack = []
    r = 0
    stack.append(c)
    visited[c] = 1

    while stack:
        c = stack.pop()
        if c-1 >= 0 and L[r][c-1] and not visited[c-1]:
            visited[c-1] = 1
            stack.append(c-1)
        elif c+1 < 100 and L[r][c+1] and not visited[c+1]:
            visited[c+1] = 1
            stack.append(c+1)
        elif r < 99:
            visited = [0] * 101
            visited[c] = 1
            stack.append(c)
            r += 1
        else:
            if L[r][c] == 2:
                return True
    return False



for _ in range(1, 11):
    t = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if L[0][i]:
            if dfs(i):
                print('#{} {}'.format(t, i))
                break