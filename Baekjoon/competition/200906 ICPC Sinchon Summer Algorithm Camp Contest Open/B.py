from sys import stdin


N, M = map(int, stdin.readline().split())
STD = [stdin.readline().split() for _ in range(N)]
power_list = [int(stdin.readline()) for _ in range(M)]
MAX = int(STD[-1][1])
stats = [0] * (MAX+1)
for word, num in reversed(STD):
    stats[int(num)] = word


for i in range(len(stats)-2 , -1, -1):
    if not stats[i]:
        stats[i] = stats[i+1]


for power in power_list:
    print(stats[power])
