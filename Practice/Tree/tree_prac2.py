'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(node):
    global cnt
    if node:
        cnt += 1
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])


V = int(input()) # 13
edges = list(map(int, input().split())) # [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
tree = [[0] * 3 for _ in range(V+1)]
E = V - 1
cnt = 0
for i in range(E):
    s, e = edges[i*2], edges[i*2+1]
    if not tree[s][0]:
        tree[s][0] = e
    else:
        tree[s][1] = e
    tree[e][2] = s
preorder(1)
print(cnt)