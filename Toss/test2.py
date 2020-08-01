# 자연수 k와 n을 입력받아, 1부터 n2 까지의 수가 달팽이 등껍질 모양(시계 방향)으로 출력되는 프로그램을 작성해주십시오.

# 자연수 k는 1부터 4까지의 자연수이며, k에 따라 출발 지점이 변경됩니다.

# - k가 1이면, 왼쪽 위에서 출발

# - k가 2이면, 오른쪽 위에서 출발

# - k가 3이면, 오른쪽 아래에서 출발

# - k가 4이면, 왼쪽 아래에서 출발

# 예를 들어 k=1, n=5가 입력되었을 때, 1부터 25까지의 수가 5 × 5 형태의 2차원 배열에 달팽이 등껍질 모양으로 정렬되어 다음과 같은 형태로 출력되어야 합니다. 

#     1    2    3    4    5
#    16   17   18   19    6
#    15   24   25   20    7
#    14   23   22   21    8
#    13   12   11   10    9


# 만약  k=2, n=5 이면,

#    13   14   15   16    1
#    12   23   24   17    2
#    11   22   25   18    3
#    10   21   20   19    4
#     9    8    7    6    5


# 만약  k=3, n=5 이면,

#     9   10   11   12   13
#     8   21   22   23   14
#     7   20   25   24   15
#     6   19   18   17   16
#     5    4    3    2    1


# 만약  k=4, n=5 이면,

#     5    6    7    8    9
#     4   19   20   21   10
#     3   18   25   22   11
#     2   17   24   23   12
#     1   16   15   14   13


# 입력 설명

# 두 정수 k, n (k는 1이상 4 이하의 자연수, n은 15 이하의 자연수)
# 출력 설명

# k에 따라 달라지는 출발점에서 1부터 n2 까지의 수를 달팽이 등껍질 모양으로 정렬한 2차원 배열 (n × n) 출력

# user_input = list(map(int, input().split())
# try:
#     k = user_input[0]
#     n = user_input[1]
# except:
#     print("IndexError")
user_input = list(map(int, input().split()))
k = user_input[0]
n = user_input[1]
if k == 1:
    a, b, direction = 1, 1, 1
elif k == 2:
    a, b, direction = 1, 5, 2
elif k == 3:
    a, b, direction = 5, 5, 3
else:
    a, b, direction = 5, 1, 4

d = dict()
i = 1
first_contact = 4
x1 = y1 = 2
x2 = y2 = n
while i < n**2+1:
    try:
        d[a, b] += 0
    except:
        d[a, b] = i
        i += 1
    if direction == 1:
        b += 1
        if b > x2-1:
            direction = direction + 1 if direction < 4 else 1
            x2 -= 1
    elif direction == 2:
        a += 1
        if a > y2-1:
            direction = direction + 1 if direction < 4 else 1
            y2 -= 1
    elif direction == 3:
        b -= 1
        if b < x1:
            direction = direction + 1 if direction < 4 else 1
            x1 += 1
    else:
        a -= 1
        if a < y1:
            direction = direction + 1 if direction < 4 else 1
            y1 += 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i, j] < 10:
            print('   ', d[i, j], end='')
        else:
            print('  ', d[i, j], end='')
        if j == n:
            print()