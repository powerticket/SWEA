K = int(input())
location = []
max_dist = 0
max_idx = 0
for _ in range(6):
    location.append(list(map(int, input().split())))
for i in range(6):
    distance = location[i][1]
    if distance > max_dist:
        max_dist = distance
        max_idx = i
down = (max_idx-1) % 6
up = (max_idx+1) % 6
if location[down][1] > location[up][1]:
    area = max_dist * location[down][1] - location[(down-2)%6][1] * location[(max_idx+2)%6][1]
else:
    area = max_dist * location[up][1] - location[(up+2)%6][1] * location[(max_idx-2)%6][1]
result = area * K
print(result)
