from pwn import xor
ct = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(0, 256):
    pt = xor(ct, i)
    if b"crypto{" in pt:
        print(pt)
        print(i)
        break