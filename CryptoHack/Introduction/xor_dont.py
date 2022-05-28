from pwn import xor
ct = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = "myXORkey"
for i in range(60, 127):
    pt = xor(ct, key + chr(i))
    #print(i, ":", pt)
    if b'crypto{}' in pt:
        print(pt)
        key += chr(i)
        break

print(xor(ct, key))