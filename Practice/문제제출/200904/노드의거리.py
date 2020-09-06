for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1
    
    s, e = map(int, input().split())

    visit = [0] * (V+1)
    Q = [s]
    visit[s] = 1

    while Q:
        v = Q.pop(0)
        # v가 도착점이면 빠져나감
        # if v == e:
        #     break
        for w in range(1, V+1):
            if G[v][w] and not visit[w]:
                visit[w] = visit[v] + 1
                # w가 도착점이면 빠져나감
                # if w == e:
                #     Q.clear()
                #     break
                Q.append(w)
    
    print(visit[e]-1)