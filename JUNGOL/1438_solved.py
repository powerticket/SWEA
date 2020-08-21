l = [[0] * 100 for _ in range(100)]
N = int(input())
# N = 3
input_paper = [list(map(int, input().split())) for _ in range(N)]
# input_paper = [[3, 7], [15, 7], [5, 2]]
for i in range(N):
    x = input_paper[i][0] - 1
    y = input_paper[i][1] - 1
    for j in range(10):
        for k in range(10):
            l[x+j][y+k] = 1
total = 0
for i in range(100):
    total += sum(l[i])
print(total)