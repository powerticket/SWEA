input_list = []
arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    input_list.append(list(map(int, input().split())))
for x1, y1, x2, y2 in input_list:
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
area = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j]:
            area += 1
print(area)