V, E = map(int, input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    n1, n2, c = map(int, input().split())
    adj[n1].append((n2, c))
INF = 0xffffff
dist = [INF] * V
selected = [False] * V
dist[0] = 0
cnt = 0
while cnt < V:
    minV = INF
    u = -1
    for i in range(V):
        if not selected[i] and minV > dist[i]:
            minV = dist[i]
            u = i
    selected[u] = True
    cnt += 1
    for w, cost in adj[u]:
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
print(dist)
