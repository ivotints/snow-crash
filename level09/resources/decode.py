with open("token", 'rb') as f:
    cipher = f.read()

for i in range(len(cipher)):
    val = cipher[i] - i
    if 0 <= val < 255:
        print(chr(val), end='')
print()
