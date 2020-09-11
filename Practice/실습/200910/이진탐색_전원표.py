# binary tree search
def bts(n):
    global value
    if tree[n][1]:
        bts(tree[n][1])
    value += 1
    tree[n][3] = value
    if tree[n][2]:
        bts(tree[n][2])


for t in range(1, int(input())+1):
    value = 0
    N = int(input())
    tree = [[0] * 4 for _ in range(N+1)]
    for i in range(1, N+1):
        tree[i][0] = i // 2
        if i*2 <= N:
            tree[i][1] = i * 2
        if i*2+1 <= N:
            tree[i][2] = i * 2 + 1
    bts(1)
    print('#{}'.format(t), tree[1][3], tree[N//2][3])