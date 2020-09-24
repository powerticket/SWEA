x, y = map(int, input().split())
N = int(input())
# 가로, 세로 절단면을 저장할 리스트를 생성하고 처음과 끝 값을 저장
x_cut = [0, x]
y_cut = [0, y]
# 가로, 세로 절단면을 입력받고 해당 리스트에 저장
for _ in range(N):
    d, cut = map(int, input().split())
    if d:
        x_cut.append(cut)
    else:
        y_cut.append(cut)
x_max = 1
y_max = 1
# 연산을 용이하게 하기 위해서 내림차순으로 정렬
x_cut.sort(reverse=True)
y_cut.sort(reverse=True)
len_x_cut = len(x_cut)
len_y_cut = len(y_cut)
# 가로, 세로 절단 리스트를 돌면서 최대 차이 확인
for i in range(len_x_cut-1):
    diff = x_cut[i] - x_cut[i+1]
    if diff > x_max:
        x_max = diff
for i in range(len_y_cut-1):
    diff = y_cut[i] - y_cut[i+1]
    if diff > y_max:
        y_max = diff
# 확인된 최대 차이의 곱을 출력
print(x_max*y_max)