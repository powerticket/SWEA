def dfs(idx, result):
    if idx == N-1:
        global maxV, minV
        if result > maxV:
            maxV = result
        if result < minV:
            minV = result
        return
    for i in range(4):
        if op[i]:
            op[i] -= 1
            if i == 0:
                dfs(idx+1, result + num[idx+1])
            elif i == 1:
                dfs(idx+1, result - num[idx+1])
            elif i == 2:
                dfs(idx+1, result * num[idx+1])
            else:
                dfs(idx+1, int(result / num[idx+1]))
            op[i] += 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))
    maxV = -0xffffffff
    minV = 0xffffffff
    dfs(0, num[0])
    print('#{} {}'.format(t, maxV-minV))
