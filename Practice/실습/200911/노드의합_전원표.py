def bts(v):
    if v > N:
        return 0
    tree[v] += bts(v * 2) + bts(v * 2 + 1)
    return tree[v]


for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    bts(1)
    print('#{} {}'.format(t, tree[L]))