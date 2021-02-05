# 01/29
# 4191 Dominos 2

from collections import deque

T = int(input())
for _ in range(T):
    n, m, l = map(int, input().split())
    # 도미노가 넘어졌는지 확인하는 배열 생성
    dominos = [0] * (n+1)
    # 해당 도미노가 넘어지면 따라 넘어지는 도미노를 담은 배열 생성
    series = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        series[x].append(y)
    # 손으로 넘어뜨린 도미노 배열 생성
    falls = deque()
    for _ in range(l):
        z = int(input())
        # 넘어진 도미노는 1로 변경
        dominos[z] = 1
        falls.append(z)
    # 손으로 넘어뜨릴 도미노가 남아있을 때까지 while 반복
    while falls:
        fall = falls.popleft()
        dominos[fall] = 1
        # 해당 도미노가 넘어트릴 다음 도미노들을 순회하며 아직 넘어짐 체크를 안했을 경우 넘어지는 도미노 배열에 추가하고 해당 도미노 배열을 1로 변경
        for next_fall in series[fall]:
            if not dominos[next_fall]:
                dominos[next_fall] = 1
                falls.append(next_fall)
    # 넘어진 도미노의 합 출력
    print(sum(dominos))
