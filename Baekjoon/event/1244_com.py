N = int(input())
# 스위치 인덱스를 해당 숫자로 접근하기 위해서 앞에 0을 추가한 리스트를 생성한다.
switch = [0] + list(map(int, input().split()))
for _ in range(int(input())):
    gender, number = map(int, input().split())
    # 번호를 뽑은 학생이 남학생일 경우 해당 배수의 스위치의 상태를 바꾼다.
    if gender == 1:
        for i in range(number, N+1, number):
            switch[i] = int(not switch[i])
    #  번호를 뽑은 학생이 여학생일 경우 좌우가 대칭인 구간의 스위치 상태를 전부 바꾼다.
    else:
        switch[number] = int(not switch[number])
        left = number - 1
        right = number + 1
        while left > 0 and right < N+1 and switch[left] == switch[right]:
            switch[left] = int(not switch[left])
            switch[right] = int(not switch[right])
            left -= 1
            right += 1
# 한 줄에 스위치 20개씩 출력한다.
for i in range(1, N, 20):
    print(*switch[i:i+20])