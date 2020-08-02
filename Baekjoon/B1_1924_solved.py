L = list(map(int, input().split()))

m = L[0]
d = L[1]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
count = 0
for i in range(1, m):
    if i == 2:
        count += 28
    elif i in [4, 6, 9, 11]:
        count += 30
    else:
        count += 31
count += d
print(day[count%7])