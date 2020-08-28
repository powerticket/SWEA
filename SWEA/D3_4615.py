import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
def oth(r, c, s):



for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    B = [[0] * N for _ in range(N)]
    B[N//2-1][N//2], B[N//2][N//2-1] = 1, 1
    B[N//2-1][N//2-1], B[N//2][N//2] = 2, 2
    for r, c, s in arr:
        for d in range(8):
            oth(r, c, s)
    print(B)