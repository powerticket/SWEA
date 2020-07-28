# T = int(input())
# for testcase in range(T):
#     N = int(input())
#     print("#%d" %(testcase+1))
#     namebook = [[0] for _ in range(100)]
#     for _ in range(N):
#         temp = input().strip()
#         namebook[len(temp)-1][0] += 1
#         namebook[len(temp)-1].append(temp)
#     for i in range(100):
#         if namebook[i][0] > 0:
#             temp_list = list(set(namebook[i][1:]))
#             temp_list.sort()
#             namebook[i][1:] = temp_list
#             namebook[i][0] = len(temp_list)
#     for i in range(100):
#         for j in range(namebook[i][0]):
#             print(namebook[i][j+1])

namebook = [[] for _ in range(100)]
print(namebook)