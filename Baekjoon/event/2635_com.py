N = int(input())
max_cnt = 3
max_num = 1
# 1부터 N까지의 수를 순회
for i in range(1, N+1):
    n1 = N
    n2 = i
    cnt = 2
    # 앞의 수가 뒤의 수보다 작아질 때까지 반복
    while n1 >= n2:
        n1, n2 = n2, n1 - n2
        cnt += 1
    # 반복수가 최대일 경우 해당 횟수 및 숫자 저장
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = i
n1, n2 = N, max_num
# 최대 연속 수 및 해당 숫자 출력
print(max_cnt)
print(n1, n2, end=' ')
for _ in range(max_cnt-2):
    print(n1-n2, end=' ')
    n1, n2 = n2, n1 - n2
