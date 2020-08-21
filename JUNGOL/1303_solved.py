N, M = map(int, input().split())
result = 0
for i in range(N):
    for j in range(M):
        result += 1
        print(result, end=' ')
    print()