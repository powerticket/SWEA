import sys
sys.stdin = open('0316_3190.txt', 'r')

# 03/16
# 3190 뱀

N = int(input())
K = int(input())
apple = [[0] * N for _ in range(N)]

# 사과 배치
for _ in range(K):
    r, c = map(int, input().split())
    apple[r-1][c-1] = 1

L = int(input())
snake_move = []
for _ in range(L):
    time, direction = input().split()
    snake_move.append((int(time), direction))

# 뱀의 몸 배열
snake = [[0] * N for _ in range(N)]
snake[0][0] = 1
# 뱀의 머리부터 꼬리까지 queue로 구현
snake_queue = [(0, 0)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = 0
snake_r = snake_c = 0
cur_d = 0
time, next_d = snake_move.pop(0)
while 1:
    # 현재 시간이 뱀이 움직임을 전환할 시간이 됐으면, 방향 전환
    if result == time:
        if next_d == 'L':
            cur_d = (cur_d - 1) % 4
        else:
            cur_d = (cur_d + 1) % 4
        # 다음 움직임이 남아있으면 time, next_d 변수에 저장
        if snake_move:
            time, next_d = snake_move.pop(0)
    # 시간 증가
    result += 1
    # 뱀 머리 이동
    snake_r += direction[cur_d][0]
    snake_c += direction[cur_d][1]
    # 뱀이 벽이나 몸통에 부딪히지 않으면 이동
    if 0 <= snake_r < N and 0 <= snake_c < N and not snake[snake_r][snake_c]:
        snake_queue.append((snake_r, snake_c))
        snake[snake_r][snake_c] = 1
        # 사과 냠냠
        if apple[snake_r][snake_c]:
            apple[snake_r][snake_c] = 0
        # 사과를 못 먹으면 몸 길이 줄임
        else:
            tail_r, tail_c = snake_queue.pop(0)
            snake[tail_r][tail_c] = 0
    else:
        break

print(result)
