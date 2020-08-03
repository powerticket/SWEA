T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    sos = [0] * (N-M+1)
    for i in range(N-M+1):
        sos[i] += sum(L[i:i+M])
    print(f'#{t} {max(sos)-min(sos)}')
