ptn = ['W', 'B', 'R']
def check(row, color):
    return M - flag[row].count(ptn[color])


def dfs(row, color, cur_sum):
    cur_sum += check(row, color)
    if row == N-2:
        global min_sum
        min_sum = min(min_sum, cur_sum)
        return
    if cur_sum > min_sum:
        return
    if color == 0 and row == N-3:
        dfs(row+1, color+1, cur_sum)
    elif color != 2:
        dfs(row+1, color, cur_sum)
        dfs(row+1, color+1, cur_sum)
    else:
        dfs(row+1, color, cur_sum)


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_sum = N * M
    dfs(0, 0, 0)
    min_sum += M - flag[-1].count(ptn[-1])
    print('#{} {}'.format(t, min_sum))
