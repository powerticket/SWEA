from collections import deque


def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def compareParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    return a == b


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    rel = [list(map(int, input().split())) for _ in range(E)]
    rel.sort(key=lambda x: x[2])
    parent = list(range(V+1))
    result = 0
    cnt = 0
    for start, end, cost in rel:
        if not compareParent(parent, start, end):
            unionParent(parent, start, end)
            result += cost
            cnt += 1
        if cnt == V:
            break
    print('#{} {}'.format(t, result))
