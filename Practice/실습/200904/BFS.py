'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(v):
    visited = [0] * (V+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
    print(visited)


V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(V+1)]
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)

bfs(1)
