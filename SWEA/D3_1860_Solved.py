import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    client = list(map(int, input().split()))
    sec = [0]
    for i in range(1, max(client)+1):
        if i % M == 0:
            sec += [K]
        else:
            sec += [0]
    for i in range(len(sec)-1):
        sec[i+1] += sec[i]
    for c in sorted(client):
        for i in range(c, len(sec)):
            sec[i] -= 1
        if sec[c] == -1:
            print('#{} Impossible'.format(t))
            break
    else:
        print('#{} Possible'.format(t))
