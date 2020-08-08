import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    L.sort()
    max_dia = 0
    for i in range(N-1):
        count = 0
        for j in range(i, N):
            if L[j] - L[i] <= K:
                count += 1
        if count > max_dia:
            max_dia = count
    print('#{} {}'.format(t, max_dia))