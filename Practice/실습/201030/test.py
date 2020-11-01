for a in "abcdefghijklmnopqrstuvwxyz":
    for b in "abcdefghijklmnopqrstuvwxyz":
        print(chr((ord(a) - ord(b) - 1) % 26 + 97), a, b)