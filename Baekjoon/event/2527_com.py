for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # 가로, 세로 좌표 중 한군데라도 겹치는 곳이 없으면 공통부분이 없음
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        result = 'd'
    # 가로, 세로 좌표의 각 꼭지점이 같은 좌표일 경우 점
    elif p1 == x2 and (q1 == y2 or q2 == y1) or p2 == x1 and (q2 == y1 or q1 == y2):
        result = 'c'
    # 위의 조건이 아니면서 모든 꼭지점중 한군데가 같을 경우 선분
    elif p1 == x2 or q1 == y2 or p2 == x1 or q2 == y1:
        result = 'b'
    # 위의 모든 조건이 해당되지 않으면 직사각형
    else:
        result = 'a'
    print(result)
