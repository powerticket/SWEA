# 동, 서, 남, 북 = 4, 3, 2, 1
X, Y = map(int, input().split())
N = int(input())
store = [[0] * (X+1) for _ in range(Y+1)]
# 방향과 거리에 따라 상점의 좌표를 설정해준다
for _ in ' '*N:
    direction, distance = map(int, input().split())
    if direction == 1:
        store[0][distance] = 1
    elif direction == 2:
        store[Y][distance] = 1
    elif direction == 3:
        store[distance][0] = 1
    elif direction == 4:
        store[distance][X] = 1
# 방향과 거리에 따라 동근이의 좌표를 설정해준다
my_dir, my_dist = map(int, input().split())
if my_dir == 1:
    my_location = (0, my_dist)
elif my_dir == 2:
    my_location = (Y, my_dist)
elif my_dir == 3:
    my_location = (my_dist, 0)
elif my_dir == 4:
    my_location = (my_dist, X)
result = 0
# 배열을 순회하며 상점이 있을 경우, 각 행, 열과 동근이 좌표의 차이를 출력한다
# 단, 가로 길이, 혹은 세로 길이가 같을 경우, 최단 거리를 확인하여 결과값에 더한다.
for i in range(Y+1):
    for j in range(X+1):
        if store[i][j]:
            y = abs(i - my_location[0])
            x = abs(j - my_location[1])
            if x == X:
                result += X + min(i + my_location[0], 2*Y - (i + my_location[0]))
            elif y == Y:
                result += Y + min(j + my_location[1], 2*X - (j + my_location[1]))
            else:
                result += x + y
print(result)