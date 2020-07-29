first_n = str(input())
if int(first_n) < 10:
    first_n = '0' + first_n
n = first_n
new_n = str()
result = 1

while 1:
    if int(n) < 10:
        n = '0' + str(int(n))
    new_n = str(int(n[0]) + int(n[1]))
    if int(new_n) < 10:
        new_n = '0' + str(int(new_n))
    n = n[1] + new_n[1]
    if first_n == n:
        break
    result += 1
print(result)