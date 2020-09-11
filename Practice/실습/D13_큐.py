import sys
sys.stdin = open('sample_input.txt', 'r')


T = ['S', 'D', 'H', 'C']
for t in range(1, int(input())+1):
    S = input()
    N = len(S)
    cnt = [13] * 4
    v = [[0] * 14 for _ in range(4)]
    for i in range(0, N, 3):
        if not v[T.index(S[i])][int(S[i+1:i+3])]:
            v[T.index(S[i])][int(S[i+1:i+3])] = 1
            cnt[T.index(S[i])] -= 1
        else:
            break
    else:
        print('#{} {} {} {} {}'.format(t, *cnt))
        print()
        continue
    print('#{} ERROR'.format(t))