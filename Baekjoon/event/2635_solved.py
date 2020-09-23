N = int(input())
max_cnt = 3
max_num = 1
for i in range(1, N+1):
    n1 = N
    n2 = i
    cnt = 2
    while n1 >= n2:
        n1, n2 = n2, n1 - n2
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = i
n1, n2 = N, max_num
print(max_cnt)
print(n1, n2, end=' ')
for _ in range(max_cnt-2):
    print(n1-n2, end=' ')
    n1, n2 = n2, n1 - n2
