def preorder(n):
    global result
    result += 1
    if tree[n][1]:
        preorder(tree[n][1])
    if tree[n][2]:
        preorder(tree[n][2])


for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E+2)]
    for i in range(E):
        p, c = edges[2*i], edges[2*i+1]
        if not tree[p][1]:
            tree[p][1] = c
        else:
            tree[p][2] = c
        tree[c][0] = p
    result = 0
    preorder(N)
    print('#{} {}'.format(t, result))