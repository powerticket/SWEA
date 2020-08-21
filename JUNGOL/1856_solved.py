N, M = map(int, input().split())
result = 0
l = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        result += 1
        l[i][j] = result

for i in range(N):
    for j in range(M):
        print(l[i][j+(-1-2*j)*(i%2)], end=' ')
    print()
