for t in range(1, int(input())+1):
    N = int(input())
    L = list(map(int, input().split()))
    avg = sum(L) / N
    cnt = 0
    for l in L:
        if l <= avg:
            cnt += 1
    print(f'#{t} {cnt}')