def findTeam(team, x):
    if team[x] == x:
        return x
    team[x] = findTeam(team, team[x])
    return team[x]


def unionTeam(team, a, b):
    a = findTeam(team, a)
    b = findTeam(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    team = list(range(N+1))
    count = [0] * (N+1)
    for i in range(M):
        a, b = arr[2*i], arr[2*i+1]
        unionTeam(team, a, b)
    for i in range(N+1):
        findTeam(team, i)
    for i in range(1, N+1):
        count[team[i]] = 1
    result = sum(count)
    print('#{} {}'.format(t, result))
