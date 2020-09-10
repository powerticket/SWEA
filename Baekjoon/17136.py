def check(r, c):
    global result
    result += 1
    for p in range(1, 6):
        temp = 0
        for i in range(p):
            for j in range(p):
                if arr[i][j]:
                    temp += 1
        if temp != p ** 2:
            for i in range(p-1):
                for j in range(p-1):
                    arr[i][j] = 0
            paper[p-1] -= 1
            break

arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
result = 0
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            check(i, j)
print(result)
