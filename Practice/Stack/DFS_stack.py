"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


def dfs(n):
    visited = [False] * (V + 1)
    stack = [0] * V
    top = -1

    top += 1
    stack[top] = n
    visited[n] = True

    while top > -1:
        n = stack[top]
        top -= 1
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and not visited[i]:
                top += 1
                stack[top] = i
                visited[i] = True


V, E = 7, 8 # map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7] # list(map(int, input().split()))

for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    adj[n1][n2], adj[n2][n1] = 1, 1

dfs(1)