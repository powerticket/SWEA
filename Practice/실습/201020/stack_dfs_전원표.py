'''
스택을 이용한 dfs

정점, 간선수
간선정보
시작점 : 1

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력결과

1 3 7 6 5 4 2

'''

def dfs(v):
    print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(w)

N, M = 7, 8
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[] for _ in range(N+1)]
for i in range(M):
    s, e = edges[2*i], edges[2*i+1]
    G[s].append(e)
    G[e].append(s)

visited = [0] * (N+1)
visited[1] = 1
dfs(1)
print()

visited = [0] * (N+1)
visited[1] = 1
stack = [1]
while stack:
    v = stack.pop()
    print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            stack.append(w)
            visited[w] = 1
print()

visited = [0] * (N+1)
visited[1] = 1
queue = [1]
while queue:
    v = queue.pop(0)
    print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            queue.append(w)
            visited[w] = 1
print()
