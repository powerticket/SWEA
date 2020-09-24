N = int(input())
board = [[0] * 101 for _ in range(101)]
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
for x1, y1, w, h in paper:
    for i in range(x1, x1+w):
        for j in range(y1, y1+h):
            board[i][j] = 1
results = []
for x1, y1, w, h in reversed(paper):
    cnt = 0
    for i in range(x1, x1+w):
        for j in range(y1, y1+h):
            if board[i][j]:
                board[i][j] = 0
                cnt += 1
    results.append(cnt)
for result in reversed(results):
    print(result)