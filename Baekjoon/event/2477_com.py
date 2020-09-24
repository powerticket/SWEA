K = int(input())
location = []
max_dist = 0
max_idx = 0
for _ in range(6):
    location.append(list(map(int, input().split())))
# 모든 면중 최댓값과 그 값의 인덱스를 확인
for i in range(6):
    distance = location[i][1]
    if distance > max_dist:
        max_dist = distance
        max_idx = i
# 최댓값의 양쪽 인덱스로 접근했을 때 더 큰 값 확인
down = (max_idx-1) % 6
up = (max_idx+1) % 6
# 최댓값의 왼쪽이 더 클 경우 최댓값 왼쪽 인덱스 -2와 최댓값 인덱스 +2의 인덱스 값의 곱을 전체 크기에서 빼준다.
if location[down][1] > location[up][1]:
    area = max_dist * location[down][1] - location[(down-2)%6][1] * location[(max_idx+2)%6][1]
# 최댓값의 오른쪽이 더 클 경우 최댓값 인덱스 -2와 최댓값 오른쪽 인덱스 +2의 인덱스 값의 곱을 전체 크기에서 빼준다.
else:
    area = max_dist * location[up][1] - location[(up+2)%6][1] * location[(max_idx-2)%6][1]
result = area * K
print(result)
