'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
edges = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edges[2*i], edges[2*i+1]
    adj[n1][n2], adj[n2][n1] = 1, 1

for row in adj:
    print(row)