import sys
import time


start = time.time()  # 시작 시간 저장
sys.stdin = open('sample_input.txt', 'r')
for tc in range(1, 1 + int(input())):
    n = int(input())
    scores = list(map(int, input().split()))

    my_scores = [0] * (sum(scores) + 1)
    my_scores[0] = 1

    for score in scores:
        for i in range(len(my_scores) - score, -1, -1):
            if my_scores[i]:
                my_scores[i + score] = 1

    print('#{} {}'.format(tc, sum(my_scores)))
print(time.time()-start)