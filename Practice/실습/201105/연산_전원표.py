from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    time = 0
    q = deque()
    visited = [0] * 1000001
    q.append(N)
    visited[N] = 1
    i = 1
    cycle = len(q)
    while q:
        if cycle != i:
            i += 1
        else:
            time += 1
            i = 1
            cycle = len(q)
        n = q.popleft()
        calculate = [n+1, n-1, n*2, n-10]
        for cal in calculate:
            if cal == M:
                break
            elif 0 <= cal < 1000001 and not visited[cal]:
                visited[cal] = 1
                q.append(cal)
        else:
            continue
        break                
    print('#{} {}'.format(t, time))
