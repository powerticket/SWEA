N = int(input())
paper = []
board = [[0] * 100 for _ in ' '*100]
# 모든 색종이의 좌표 입력
for n in range(N):
    paper.append(list(map(int, input().split())))
# 입력 받은 모든 색종이의 좌표부터 10 x 10 크기만큼 해당 위치 도화지의 값을 1로 변경
while paper:
    r, c = paper.pop(0)
    for i in range(10):
        for j in range(10):
            board[r+i][c+j] = 1
# 도화지의 모든 값의 합을 출력
print(sum(map(sum, board)))