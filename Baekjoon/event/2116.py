N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
max_result = N
for i in range(6):
    result = 0
    floor = i
    for j in range(1, N):
        floor = 
        if floor == 0:
            next_floor = 5
        elif floor == 1:
            next_floor = 3
        elif floor == 2:
            next_floor = 4
        elif floor == 3:
            next_floor = 1
        elif floor == 4:
            next_floor = 2
        elif floor == 5:
            next_floor = 0
        result += max([i for i in range(1, 7) if i not in (dice[j][floor], dice[j][next_floor])])
    if result > max_result:
        max_result = result
print(max_result)