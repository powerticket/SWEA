# 난쟁이 입력
dwarfs = [int(input()) for _ in ' '*9]

# Bubble Sort를 이용하여 오름차순 정렬
for i in range(8, 0, -1):
    for j in range(i):
        if dwarfs[j] > dwarfs[j+1]:
            dwarfs[j], dwarfs[j+1] = dwarfs[j+1], dwarfs[j]

# 난쟁이의 총합 확인
total = 0
for dwarf in dwarfs:
    total += dwarf

# 두 난쟁이를 뺀 합이 100이면 가짜 난쟁이 확인 후 반복문 종료
for fake1 in dwarfs:
    for fake2 in dwarfs:
        if fake1 != fake2:
            if total - fake1 - fake2 == 100:
                fake = (fake1, fake2)
                break
    else:
        continue
    break

# 진짜 난쟁이 출력
for dwarf in dwarfs:
    if dwarf not in fake:
        print(dwarf)