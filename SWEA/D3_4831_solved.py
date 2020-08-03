T = int(input())

for t in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    charge = [0] * (N+K+1)
    for l in L:
        charge[l] += 1
    distance = K
    count = 0
    for i in range(N+1):
        if distance == -1:
            print(f'#{t} 0')
            break
        ok = 0
        if N - i <= distance:
            ok = 1
        for d in range(1, distance+1):
            if charge[i+d] == 1:
                ok = 1
        if ok == 0:
            if charge[i] == 1:
                ok = 1
                count += 1
                distance = K
        distance -= 1
    else:
        print(f'#{t} {count}')