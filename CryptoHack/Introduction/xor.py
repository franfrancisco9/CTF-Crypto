def xor(a, b):
    xored = []
    for i in range(len(a)):
        xored_value = ord(a[i%len(a)]) ^ b
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)

string = xor("label", 13)
print(b"crypto{"+ bytes.fromhex(string) + b"}")