# 02/03
# 17472 다리 만들기 2

# 섬의 갯수 확인
# 각 섬에서 다른 섬으로 가는 길 및 길이 확인
# 최소 거리 순으로 정렬
# 크루스칼 알고리즘 적용

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 다리 공사
def build_bridge(r, c):
    for dr, dc in direction:
        nr = r + dr
        nc = c + dc
        distance = 0
        while 0 <= nr < N and 0 <= nc < M:
            if not arr[nr][nc]:
                distance += 1
            else:
                if distance > 1:
                    start = visited[r][c]
                    end = visited[nr][nc]
                    G[start][end] = min(G[start][end], distance)
                    G[end][start] = min(G[start][end], distance)
                break
            nr += dr
            nc += dc


# 섬 번호 매기기
def number_isle(r, c):
    for dr, dc in direction:
        nc = c + dc
        nr = r + dr
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = number
                number_isle(nr, nc)


# 서로소
# 부모 확인
def find_parant(x):
    if x != parent[x]:
        parent[x] = find_parant(parent[x])
    return parent[x]


# 부모 비교
def compare_parent(x, y):
    return find_parant(x) == find_parant(y)


# 부모 묶기
def same_parent(x, y):
    a = find_parant(x)
    b = find_parant(y)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


# 섬의 갯수 확인 및 섬 번호 지정
number = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            number += 1
            visited[i][j] = number
            number_isle(i, j)
# 다리 공사
MAX_DISTANCE = 100
G = [[MAX_DISTANCE] * (number + 1) for _ in range(number + 1)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            build_bridge(i, j)
# 중복 제거
candidate = []
for i in range(1, number+1):
    for j in range(i+1, number+1):
        if G[i][j] != MAX_DISTANCE:
            candidate.append((G[i][j], i, j))
# 다리 건설 비용 오름차순 정렬
candidate.sort()
# 부모 배열 생성
parent = list(range(number+1))
result = 0
# 후보군 순회하며 서로소일 경우, 값을 더하고 공통 집합으로 묶기
for dist, a, b in candidate:
    if not compare_parent(a, b):
        same_parent(a, b)
        result += dist
# 후보군을 전부 순회 후, 서로소 집합이 존재할 시 -1 출력
for i in range(1, number):
    if not compare_parent(i, i+1):
        result = -1
        break
print(result)
