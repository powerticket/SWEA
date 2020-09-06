W0, I0, T = map(int, input().split())
P, I_eat, A = map(int, input().split())

cur_weight = W0
cur_I = I0
for _ in range(P):
    delta = I_eat - (I0 + A)
    cur_weight += delta
    if cur_weight <= 0:
        print('Danger Diet')
        break
else:
    print(cur_weight, cur_I)

cur_weight = W0
for _ in range(P):
    delta = I_eat - (cur_I + A)
    cur_weight += delta
    if abs(delta) > T:
        cur_I += delta // 2
    if cur_weight <= 0 or cur_I <= 0:
        print('Danger Diet')
        break
else:
    print(cur_weight, cur_I, 'NO' if cur_I >= I0 else 'YOYO')
