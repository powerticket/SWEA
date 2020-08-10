import sys
sys.stdin = open('sample_input.txt', 'r')

for t in range(1, 1+int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    S = [0] * (sum(L)+1)
    S[0] = 1
    for l in L:
        for i in range(len(S)-1, -1, -1):
            if S[i]:
                S[i+l] = 1
    print('#{} {}'.format(t, sum(S)))