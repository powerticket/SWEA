# 02/04
# 15686 치킨 배달

from itertools import combinations

INF = 10000
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
# 일반집, 치킨집 확인
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if arr[i][j] == 1:
                house.append((i, j))
            else:
                chicken.append((i, j))
# 치킨집 수가 M 이하이면 M을 치킨집 수로 변경
if len(chicken) <= M:
    M = len(chicken)
# 전체 치킨집 중 M개를 선택하는 조합 배열 생성
candidates = combinations(chicken, M)
result = INF
# 각 조합별로 순회
for candidate in candidates:
    # 일반집에서 각 치킨집까지의 거리 확인 및 비교
    min_total = 0
    for house_r, house_c in house:
        min_dist = INF
        for chicken_r, chicken_c in candidate:
            dist = abs(house_r - chicken_r) + abs(house_c - chicken_c)
            if dist < min_dist:
                min_dist = dist
        min_total += min_dist
        if min_total >= result:
            break
    if min_total < result:
        result = min_total
print(result)
