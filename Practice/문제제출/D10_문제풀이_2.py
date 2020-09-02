import sys
sys.stdin = open('input.txt', 'r')


for t in range(int(input())):
    N, K = map(int, input().split())
    L = [input().replace(' ', '') for _ in range(N)]
    L_v = list(zip(*L))
    c = 0
    for i in range(N):
        for b in L[i].split('0'):
            if len(b) == K:
                c += 1
        for b in ''.join(L_v[i]).split('0'):
            if len(b) == K:
                c += 1
    print('#{} {}'.format(t+1, c))
