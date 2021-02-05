# 1038 감소하는 수

# 마지막 자리의 수가 이전 자리의 수보다 작은 k 자리의 수를 만들어 배열에 추가
def maker(k, cur_num):
    if k == 0:
        arr.append(cur_num)
    int_num = int(cur_num[-1])
    for i in range(int_num):
        maker(k-1, cur_num + str(i))


N = int(input())
arr = []
# 감소하는 수 중 제일 큰 수(9876543210)는 10자리이므로, 1~10자리의 감소하는 수 maker 함수 호출
for i in range(10):
    # 제일 앞 자리에는 0~9가 올 수 있다.
    for j in range(10):
        maker(i, str(j))
if N < len(arr):
    print(arr[N])
else:
    print(-1)
