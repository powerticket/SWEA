# 02/04
# 2563 색종이

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# 전체 영역 설정 100 x 100
area = [[0] * 100 for _ in range(100)]
# 입력 받은 색종이를 한장씩 순회
for row, col in paper:
    # 입력받은 행열의 좌표에서 + 10까지를 1로 표시
    for r in range(row, row + 10):
        for c in range(col, col + 10):
            area[r][c] = 1
print(sum(map(sum, area)))
