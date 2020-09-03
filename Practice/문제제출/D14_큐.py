import sys
sys.stdin = open('input.txt', 'r')


def bfs(v):
    visited[v] = 1
    queue = []
    queue.append(v)
    while queue:
        v = queue.pop(0)
        for w in range(1, N):
            if G[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = 1 + visited[v]


for t in range(1, 11):
    E, V = map(int, input().split())
    temp = list(map(int, input().split()))
    N = max(temp) + 1
    G = [[0] * N for _ in range(N)]
    for i in range(E//2):
        s, e = temp[2*i], temp[2*i+1]
        G[s][e] = 1
    visited = [0] * N
    bfs(V)
    max_v = 0
    result = 0
    for i in range(N):
        if visited[i] >= max_v:
            max_v = visited[i]
            result = i
    print('#{} {}'.format(t, result))
