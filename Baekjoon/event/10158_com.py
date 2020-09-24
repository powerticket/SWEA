w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dw = p + t
dh = q + t
# 처음 위치 + 시간을 가로 길이로 나눈 값이 홀수일 경우 총 가로 길이에서 나머지를 빼준다.
if (dw // w) % 2:
    x = w - (dw % w)
# 처음 위치 + 시간을 가로 길이로 나눈 값이 짝수일 경우 나머지를 x값으로 저장
else:
    x = dw % w
# 처음 위치 + 시간을 세로 길이로 나눈 값이 홀수일 경우 총 세로 길이에서 나머지를 빼준다.
if (dh // h) % 2:
    y = h - (dh % h)
# 처음 위치 + 시간을 세로 길이로 나눈 값이 짝수일 경우 나머지를 y값으로 저장
else:
    y = dh % h
print(x, y)