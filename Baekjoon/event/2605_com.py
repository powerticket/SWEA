# 학생수 입력
N = int(input())
# 학생이 뽑은 번호 입력
num = list(map(int, input().split()))
# 초기 오름차순 줄 저장
arr = [i+1 for i in range(N)]
# 해당 학생이 뽑은 번호의 크기만큼 앞사람과 자리 변경
for i, n in enumerate(num):
    for j in range(i, i-n, -1):
        arr[j-1], arr[j] = arr[j], arr[j-1]
# 결과 출력
print(*arr)
