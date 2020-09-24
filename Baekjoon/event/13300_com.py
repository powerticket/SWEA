N, K = map(int, input().split())
students = [[0] * 2 for _ in range(7)]
for _ in range(N):
    gender, grade = map(int, input().split())
    if gender:
        students[grade][1] += 1
    else:
        students[grade][0] += 1
result = 0
for i in range(1, 7):
    result += students[i][0] // K
    result += students[i][1] // K
    if students[i][0] % K:
        result += 1
    if students[i][1] % K:
        result += 1
print(result)