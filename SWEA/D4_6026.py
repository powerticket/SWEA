T = int(input())
for t in range(1, T+1):
    M, N = map(int, input().split())
    password = M ** N - ((M-1) ** N) * M
    print(password)