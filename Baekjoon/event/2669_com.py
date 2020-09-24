input_list = []
arr = [[0] * 101 for _ in range(101)]
# 4개의 직사각형 좌표를 입력
for _ in range(4):
    input_list.append(list(map(int, input().split())))
# 입력받은 직사각형의 좌표에 따라 도화지에 1 저장
for x1, y1, x2, y2 in input_list:
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
area = 0
# 도화지의 모든 합을 출력
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j]:
            area += 1
print(area)