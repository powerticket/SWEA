N = int(input())
paper = []
board = [[0] * 100 for _ in ' '*100]
for n in range(N):
    paper.append(list(map(int, input().split())))
while paper:
    r, c = paper.pop(0)
    for i in range(10):
        for j in range(10):
            board[r+i][c+j] = 1
print(sum(map(sum, board)))