import sys
sys.stdin = open('0311_5582.txt', 'r')

# 03/11
# 5582 공통 부분 문자열

s1 = input()
s2 = input()
len_s1 = len(s1)
len_s2 = len(s2)
# 두 문자열의 각 문자가 같은지 확인하는 배열 생성
arr = [[0] * (len_s2+1) for _ in range(len_s1+1)]
# 두 문자가 같을 경우, 각각의 이전 문자의 배열 + 1을 해당 위치에 저장
for i in range(len_s1):
    for j in range(len_s2):
        if s1[i] == s2[j]:
            arr[i+1][j+1] = arr[i][j] + 1
# 배열의 최댓값 출력
print(max(map(max, arr)))
