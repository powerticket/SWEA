CODE = ['001101', '010011', '111011', '100011', '110111', '001011', '111101', '011001', '101111']
input_code = '0DEC'  # '0269FAC9A0'  # input()
base2 = ''
for c in input_code:
    if c.isdigit():
        base2 += bin(int(c))[2:].rjust(4, '0')
    elif c == 'A':
        base2 += bin(10)[2:].rjust(4, '0')
    elif c == 'B':
        base2 += bin(11)[2:].rjust(4, '0')
    elif c == 'C':
        base2 += bin(12)[2:].rjust(4, '0')      
    elif c == 'D':
        base2 += bin(13)[2:].rjust(4, '0')
    elif c == 'E':
        base2 += bin(14)[2:].rjust(4, '0')
    elif c == 'F':
        base2 += bin(15)[2:].rjust(4, '0')
N = len(base2)
i = N - 1
decode = []
while i > 4:
    if base2[i] == '1':
        decode.append(CODE.index(base2[i-5:i+1]))
        i -= 6
    else:
        i -= 1
decode.reverse()
print(*decode)
