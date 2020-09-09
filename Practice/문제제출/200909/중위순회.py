def inorder(n):
    if len(G[n]) >= 3:
        inorder(int(G[n][2]))
    print(G[n][1], end='')
    if len(G[n]) > 3:
        inorder(int(G[n][3]))


for t in range(1, 11):
    V = int(input())
    G = [[] for _ in range(V+1)]
    for i in range(1, V+1):
        G[i] = input().split()
    print('#{} '.format(t), end='')
    inorder(1)
    print()
