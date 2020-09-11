def print_formatted(number):
    spaces = len(format(number, 'b'))
    for num in range(1, number+1):
        print(str(num).rjust(spaces, ' '), format(num, 'o').rjust(spaces, ' '), format(num, 'X').rjust(spaces, ' '), format(num, 'b').rjust(spaces, ' '))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)