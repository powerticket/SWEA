T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = list()
    for _ in range(N):
        L += [input().strip()]
    L = sorted(set(L))
        
    print(f'#{t}')
    for l in L:
        print(l)