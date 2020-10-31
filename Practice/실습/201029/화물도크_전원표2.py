T = int(input())
for t in range(1, T+1):
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x : x[1])
    ans = 1
    finish = jobs[0][1]
    for i in range(1, N):
        if jobs[i][0] >= finish:
            ans += 1
            finish = jobs[i][1]
    print(ans)
