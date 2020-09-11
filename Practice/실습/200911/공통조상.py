def find_p(v):
    if not tree[v][0]:
        return
    result.append(tree[v][0])
    find_p(tree[v][0])


def check_scale(v):
    global scale
    scale += 1
    if tree[v][1]:
        check_scale(tree[v][1])
    if tree[v][2]:
        check_scale(tree[v][2])


T = int(input())
for t in range(1, T+1):
    V, E, S1, S2 = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    for i in range(E):
        p, c = edges[i*2], edges[i*2+1]
        tree[c][0] = p
        if tree[p][1]:
            tree[p][2] = c
        else:
            tree[p][1] = c
    result = []
    find_p(S1)
    S1_parent = result[:]
    result = []
    find_p(S2)
    S2_parent = result[:]
    for i in range(len(S1_parent)):
        for j in range(len(S2_parent)):
            if S1_parent[i] == S2_parent[j]:
                sub_tree = S1_parent[i]
                break
        else:
            continue
        break
    scale = 0
    check_scale(sub_tree)
    print('#{} {} {}'.format(t, sub_tree, scale))