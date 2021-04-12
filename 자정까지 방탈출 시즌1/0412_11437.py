import sys
sys.stdin = open('0412_11437.txt', 'r')

# 04/12
# 11437 LCA

N = int(input())
rel = [list(map(int, input().split())) for _ in range(N-1)]
M = int(input())
candidate = [list(map(int, input().split())) for _ in range(M)]
node = [[] for _ in range(N+1)]
for start, end in rel:
    node[start].append(end)
    node[end].append(start)
depth = [0] * (N+1)
parent = [0] * (N+1)
queue = [1]
depth[1] = 1
parent[1] = 1
# 루트부터 트리 구성
while queue:
    v = queue.pop(0)
    for w in node[v]:
        if not depth[w]:
            depth[w] = depth[v] + 1
            parent[w] = v
            queue.append(w)
# 트리의 높이를 같게하고 비교하며 공통 조상을 탐색
for a, b in candidate:
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)
