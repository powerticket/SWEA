def dfs(s, d):
    stack = []
    visited = [0] * (V+1)
    stack.append(s)
    while stack:
        s = stack.pop()
        for i in range(1, len(G)):
            if G[s][i] and not visited[i]:
                if i == d:
                    return True
                stack.append(i)
                visited[i] = 1
    return False


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.extend(map(int, input().split()))
    start, end = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = edges[2*i], edges[2*i+1]
        G[s][e] = 1
    print('#{} {}'.format(t, int(dfs(start, end))))