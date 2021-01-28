# 01/28
# 2468 안전 영역

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 최대 높이 확인
MAX_HEIGHT = max(map(max, arr))
# 초기 최대 안전 영역 갯수는 1(모든 영역이 물에 잠기지 않았을 때)
max_count = 1
# 최대 높이인 영역만 물에 잠기지 않을 때까지 for 문 순회
for _ in range(MAX_HEIGHT-1):
    # 영역이 1씩 물에 잠김
    for i in range(N):
        for j in range(N):
            arr[i][j] -= 1
    # count 변수 및 visited 배열 초기화
    count = 0
    visited = [[0] * N for _ in range(N)]
    # 물에 잠기지 않았고 방문하지 않은 영역이 있으면 bfs 순회
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visited[i][j]:
                count += 1
                visited[i][j] = 1
                q = [(i, j)]
                while q:
                    r, c = q.pop(0)
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                q.append((nr, nc))
    if count > max_count:
        max_count = count
print(max_count)
