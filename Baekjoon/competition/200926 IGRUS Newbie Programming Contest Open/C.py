def square(exception, cur_cal, cur_cnt):
    if cur_cnt == exception:
        cur_cal -= 1
    if cur_cnt == 64:
        global result
        result = cur_cal
        return
    square(exception, cur_cal*2, cur_cnt+1)

N = int(input())
result = 0
answer = 0
for i in range(65):
    square(i, 1, 0)
    if result == N:
        answer = i
        break
print(answer)
