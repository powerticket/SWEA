# 01/27
# 1446 지름길

# 지름길 배열 중 가능한 조합을 선택해서 최소 길이인지 확인하는 함수
# cur_dist: 지름길 이용이 끝난 지점(해당 위치 이후로 시작되는 지름길만 이용 가능)
# total: cur_dist까지 지름길 및 고속도로를 이용하여 이동한 거리
# k: find_shortest 함수가 실행된 횟수
def find_shortest(cur_dist, total, k):
    # 해당 함수가 지름길 배열의 길이만큼 실행됐으면 지금까지의 total 거리 및 남은 고속도로 길이의 합을 지금까지 확인한 최단거리와 비교
    if k == len_short:
        total += D - cur_dist
        global shortest_dist
        if shortest_dist > total:
            shortest_dist = total
        return
    # 지름길을 택하지 않고 find_shortest 함수 호출
    find_shortest(cur_dist, total, k+1)
    # k번 째 배열에 들어있는 지름길을 이용할 수 있는지 확인
    if cur_dist <= short[k][0]:
        total += short[k][2] + short[k][0] - cur_dist
        cur_dist = short[k][1]
        find_shortest(cur_dist, total, k+1)


N, D = map(int, input().split())
short = []
# 시작 위치, 종료 위치가 고속도로 내에 있고, 시작 위치와 종료 위치의 차보다 실제 거리가 짧은 길만 지름길 배열에 추가
for _ in range(N):
    start, end, distance = map(int, input().split())
    if start > D or end > D or distance >= end - start:
        continue
    short.append((start, end, distance))
# 시작 위치를 오름차순으로 지름길 배열 정렬
short.sort()
len_short = len(short)
shortest_dist = D
find_shortest(0, 0, 0)
print(shortest_dist)
