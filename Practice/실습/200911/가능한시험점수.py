for t in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score)+1)
    Q = [0]

    for val in score:
        for i in range(len(Q)):
            if visit[Q[i]+val]:
                continue
            visit[Q[i]+val] = 1
            Q.append(Q[i]+val)
    print('#{} {}'.format(t, len(Q)))
