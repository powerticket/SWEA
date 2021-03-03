import sys
sys.stdin = open('0209_2252.txt', 'r')

# 02/09
# 2252 줄 세우기

N, M = map(int, input().split())
student = [[0, n] for n in range(N+1)]
relation = [[] for _ in range(N+1)]
for _ in range(M):
    fw, bw = map(int, input().split())
    student[bw][0] = max(student[bw][0], student[fw][0] + 1)
    relation[fw].append(bw)
for i in range(1, N+1):
    if relation[i]:
        for bw in relation[i]:
            student[bw][0] = max(student[bw][0], student[i][0] + 1)
student.sort()
print(*list(zip(*student[1:]))[1])
