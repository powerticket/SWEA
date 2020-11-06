def mst_prim():
    key = [0xffffffff] * (V+1)
    visited = [0] * (V+1)
    key[0] = 0
    for _ in range(V):
        min_idx = -1
        min_value = 0xffffffff
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:
                min_value = key[i]
                min_idx = i
        visited[min_idx] = 1
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < key[i]:
                key[i] = adj[min_idx][i]
    return sum(key)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0xffffffff] * (V+1) for _ in range(V+1)]
    for i in range(E):
        A, B, W = map(int, input().split())
        adj[A][B] = adj[B][A] = W
    print("#{} {}".format(t, mst_prim()))
