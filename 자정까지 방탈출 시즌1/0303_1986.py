import sys
sys.stdin = open('0303_1986.txt', 'r')

# 03/03
# 1986 체스

n, m = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

# 안전한 위치 배열
possible = [[1] * m for _ in range(n)]

# 말 배치
# Queen
for i in range(queen[0]):
    r, c = queen[2*i+1] - 1, queen[2*i+2] - 1
    possible[r][c] = -1

# Knight
for i in range(knight[0]):
    r, c = knight[2*i+1] - 1, knight[2*i+2] - 1
    possible[r][c] = -1

# Pawn
for i in range(pawn[0]):
    r, c = pawn[2*i+1] - 1, pawn[2*i+2] - 1
    possible[r][c] = -1

# 공격 가능한 위치 제거
# Queen
for i in range(queen[0]):
    r, c = queen[2*i+1] - 1, queen[2*i+2] - 1
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]:
        nr = r
        nc = c
        while 1:
            nr += dr
            nc += dc
            if 0 <= nr < n and 0 <= nc < m:
                if possible[nr][nc] == 1:
                    possible[nr][nc] = 0
                elif possible[nr][nc] == -1:
                    break
            else:
                break

# Knight
for i in range(knight[0]):
    r, c = knight[2*i+1] - 1, knight[2*i+2] - 1
    possible[r][c] = -1
    for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if possible[nr][nc] == 1:
                possible[nr][nc] = 0

result = 0
for i in range(n):
    for j in range(m):
        if possible[i][j] == 1:
            result += 1
print(result)
