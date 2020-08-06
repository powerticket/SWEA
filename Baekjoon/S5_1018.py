'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
'''
N, M = map(int, input().split())
L = [input() for _ in range(N)]
fix = [[0] * (M-7) for _ in range(N-7)]

for i in range(N):
    for j in range(M):
        if L[i][j] == 'W':
            L[i][j] = 1
        else:
            L[i][j] = -1
print(L)

# for i in range(N-7):
#     for j in range(M-7):
#         for k in range(8):
#             for l in range(8):
#                 chess[i+k][j+l]