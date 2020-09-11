'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''
T = int(input())
for t in range(1, T+1):
    deck = [13] * 4
    cards = list(input())
    isError = False
    while cards and not isError:
        ptn = cards.pop(0)
        nums = cards.pop(0)
        
