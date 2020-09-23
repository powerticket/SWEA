d = 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
C, R = map(int, input().split())
N = int(input())
num = 1
min_r = 0
max_r = R
min_c = 0
max_c = C
if N > C * R:
    print(0)
else:
    r, c = -1, 0
    for _ in range(N):
        nr = r + dr[d]
        nc = c + dc[d]
        if min_r <= nr < max_r and min_c <= nc < max_c:
            r, c = nr, nc
        else:
            if d == 0:
                min_c += 1
            elif d == 1:
                max_r -= 1
            elif d == 2:
                max_c -= 1
            elif d == 3:
                min_r += 1
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
    print(c+1, r+1)