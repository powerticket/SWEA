import sys
sys.stdin = open('sample_input.txt', 'r')


def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for w in range(1, V+1):
            if G[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = temp[i][0], temp[i][1]
        G[s][e] = G[e][s] = 1
    visited = [0] * (V+1)
    bfs(start)
    result = visited[end]
    if result:
        result -= 1
    print('#{} {}'.format(t, result))