N = int(input())
# 주사위의 갯수만큼 입력을 받고 리스트에 저장
dice = [list(map(int, input().split())) for _ in range(N)]
max_result = N
# 첫 번째 주사위의 6면을 순회하면서 최댓값 탐색
for i in range(6):
    # 주사위의 바닥면에 따라 다음 주사위와 겹치는 면 확인
    floor = i
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
    # 주사위의 바닥면과 윗면을 제외한 숫자 중 최댓값 확인하여 결과값에 저장
    result = max([i for i in range(1, 7) if i not in (dice[0][floor], dice[0][next_floor])])
    for j in range(1, N):
      # 주사위의 바닥면에 따라 다음 주사위와 겹치는 면 확인
        floor = dice[j].index(dice[j-1][next_floor])
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
        # 주사위의 바닥면에 따라 다음 주사위와 겹치는 면 확인
        result += max([i for i in range(1, 7) if i not in (dice[j][floor], dice[j][next_floor])])
    # 현재까지 확인된 최댓값과 비교
    if result > max_result:
        max_result = result
print(max_result)