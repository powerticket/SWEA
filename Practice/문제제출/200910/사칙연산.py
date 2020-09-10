def tree_cal(n):
    result = 0
    if tree[n][1].isdigit():
        return int(tree[n][1])
    else:
        if tree[n][1] == '+':
            result = tree_cal(int(tree[n][2])) + tree_cal(int(tree[n][3]))
        if tree[n][1] == '-':
            result = tree_cal(int(tree[n][2])) - tree_cal(int(tree[n][3]))
        if tree[n][1] == '*':
            result = tree_cal(int(tree[n][2])) * tree_cal(int(tree[n][3]))
        if tree[n][1] == '/':
            result = tree_cal(int(tree[n][2])) // tree_cal(int(tree[n][3]))
    return result


for t in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        tree[i] = input().split()
    result = tree_cal(1)
    print('#{} {}'.format(t, result))
