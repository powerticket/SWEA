import sys
sys.stdin = open('0205_17143.txt', 'r')

# 02/05
# 17143 낚시왕

R, C, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    # 상어가 왕복하지 않도록 속도 변경
    if shark[i][3] <= 2: 
        shark[i][2] %= 2 * R - 2
    else:
        shark[i][2] %= 2 * C - 2
result = 0
# 낚시꾼 이동
for col in range(1, C+1):
    # 상어 배치
    shark_map = [[0] * (C + 1) for _ in range(R + 1)]
    for r, c, s, d, z in shark:
        if d:
            shark_map[r][c] = max(shark_map[r][c], z)
    # 상어 낚시
    for row in range(1, R + 1):
        if shark_map[row][col]:
            result += shark_map[row][col]
            shark_map[row][col] = 0
            break
    # 상어 이동
    for i in range(M):
        r, c, s, d, z = shark[i]
        # 죽은 상어 확인
        if shark_map[r][c] != z:
            d = 0
        if d:
            for _ in range(s):
                # 상
                if d == 1:
                    if r == 1:
                        r += 1
                        d = 2
                        continue
                    r -= 1
                # 하
                elif d == 2:
                    if r == R:
                        r -= 1
                        d = 1
                        continue
                    r += 1
                # 우
                elif d == 3:
                    if c == C:
                        c -= 1
                        d = 4
                        continue
                    c += 1
                # 좌
                elif d == 4:
                    if c == 1:
                        c += 1
                        d = 3
                        continue
                    c -= 1
        shark[i] = [r, c, s, d, z]
print(result)
