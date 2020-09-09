for t in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = arr[i*2], arr[i*2+1]
        G[s][e] = 1
    result = []
    queue = []
    queue.append(1)
    visited = [0] * (V+1)
    end = 0
    while end < V:
        for i in range(1, V+1):
            if not visited[i]:
                for j in range(1, V+1):
                    if G[j][i]:
                        break
                else:
                    visited[i] = 1
                    result.append(i)
                    end += 1
                    for j in range(1, V+1):
                        G[i][j] = 0
    print('#{}'.format(t), *result)