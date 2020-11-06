from queue import PriorityQueue

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 0xffffffff
    q = PriorityQueue()
    cost = [[INF] * N for _ in range(N)]
    q.put((0, 0, 0))
    cost[0][0] = 0
    while not q.empty():
        cur_cost, r, c = q.get()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                diff = arr[nr][nc] - arr[r][c]
                if diff < 0:
                    diff = 0
                fuel = cur_cost + 1 + diff
                if cost[nr][nc] > fuel:
                    cost[nr][nc] = fuel                    
                    q.put((cost[nr][nc], nr, nc))
    print('#{} {}'.format(t, cost[N-1][N-1]))
