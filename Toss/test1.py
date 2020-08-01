# 세 정수 a, b, c 를 입력 받고,

# a ≤ n ≤ b 인 범위 내에서

# n부터 시작하여 n이 짝수일 경우 2로 나누고 홀수일 경우 3을 곱한 다음 1을 더하는 연산을 수행합니다.

# 단, 3을 곱한 다음 1을 더하는 연산의 결과가, b를 3으로 나눈 값보다 크면서 c가 0보다 큰 경우 n에 10을 추가로 더해주고, c는 1을 뺍니다. (한 사이클 내에)

# 이러한 연산을 거쳐 만들어진 숫자가 1이 될 때까지 같은 작업을 계속 반복합니다.



# n과 b가 22이고, c가 3일 경우,

# 22 11 44 22 11 44 22 11 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# 다음과 같이 연산이 수행되고, 총 사이클의 길이는 25가 됩니다. (반복 1회 당 사이클의 길이는 1)

# a, b 범위 내의 수들이 위의 연산을 수행할 때 가지는 사이클의 길이 중 최대인 길이를 구하는 프로그램을 작성하십시오.



# 입력 설명

# 세 정수 a, b, c (1 ≤ a ≤ 5000 , 1 ≤ b ≤ 5000, 0 ≤ c ≤ 100  )
# 출력 설명

# a ≤ n ≤ b 인 범위 내에서 특정 수의 최대 사이클의 길이

user_input = list(map(int, input().split()))
a_input = user_input[0]
b_input = user_input[1]
c_input = user_input[2]
cycle_list = []
for n in range(a_input, b_input+1):
    final_n = n
    cycle = 1
    c = c_input
    while final_n != 1:
        if final_n % 2 == 0:
            final_n /= 2
            cycle += 1
        else:
            final_n = 3 * final_n + 1
            if final_n > b_input/3 and c > 0:
                final_n += 10
                c -= 1
            cycle += 1
    cycle_list.append(cycle)
print(cycle_list)