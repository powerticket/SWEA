# 빙고판에서 사회자가 부른 번호를 0으로 바꾸는 check_board 함수 정의
def check_board(n):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == n:
                bingo_board[i][j] = 0
                return

# 빙고의 합이 3 이상인지 확인하는 bingo 함수 정의
def bingo():
    bingo_cnt = 0
    # 가로 빙고 확인
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] != 0:
                break
        else:
            bingo_cnt += 1
    # 세로 빙고 확인
    for i in range(5):
        for j in range(5):
            if bingo_board[j][i] != 0:
                break
        else:
            bingo_cnt += 1
    # 대각선 빙고 확인
    for i in range(5):
        if bingo_board[i][i] != 0:
            break
    else:
        bingo_cnt += 1
    for i in range(5):
        if bingo_board[i][-1-i] != 0:
            break
    else:
        bingo_cnt += 1
    # 빙고의 합이 3 이상이면 1 반환
    if bingo_cnt >= 3:
        return 1
    return 0

# 철수의 빙고판 번호 입력
bingo_board = [list(map(int, input().split())) for _ in ' '*5]
# 사회자가 부르는 수 입력
bingo_call = [list(map(int, input().split())) for _ in ' '*5]
result = 25
for i in range(5):
    for j in range(5):
        # 사회자가 부른 수를 빙고판에서 0으로 변경
        check_board(bingo_call[i][j])
        # 빙고가 3개 이상인지 확인 후, 맞을 경우 반복문 종료 후, 결과값 출력
        if bingo():
            result = 5*i + j+1
            break
    else:
        continue
    break
print(result)