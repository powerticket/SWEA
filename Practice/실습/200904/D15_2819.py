dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(row, col, cur_list):
    next_list = cur_list[:]
    next_list.append(L[row][col])
    if len(next_list) == 7:
        num_set.add(''.join(next_list))
        return

    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        dfs(nr, nc, next_list)


for t in range(1, int(input())+1):
    N = 4
    L = [input().split() for _ in range(N)]
    num_set = set()
    for i in range(N):
        for j in range(N):
            dfs(i, j, [])
    print('#{} {}'.format(t, len(num_set)))
'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''