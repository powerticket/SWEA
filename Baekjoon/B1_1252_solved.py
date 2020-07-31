def make_binary(decimal):
    if decimal < 2:
        return str(decimal)
    return make_binary(decimal//2) + str(decimal%2)

def make_decimal(binary):
    result = 0
    for i in range(len(binary)-1, -1, -1):
        result += int(binary[-1-i]) * pow(2, i)
    return result

binary_nums = input().split()
decimal_sum = make_decimal(binary_nums[0]) + make_decimal(binary_nums[1])
print(make_binary(decimal_sum))