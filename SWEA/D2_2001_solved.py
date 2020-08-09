'''
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    A = N - M + 1
    max_catch = 0
    for i in range(A):
        for j in range(A):
            catch = 0
            for k in range(M):
                for l in range(M):
                    catch += L[i+k][j+l]
            if catch > max_catch:
                max_catch = catch
    print('#{} {}'.format(t, max_catch))