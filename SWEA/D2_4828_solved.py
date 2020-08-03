T = int(input())

for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    print(f'#{t} {max(L)-min(L)}')