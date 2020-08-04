T int(input())

for t in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for i in range(N)]
    C = [[0] * 10] * 10
    for l in range(len(L)):
        