from email.mime import base
from pwn import *
import hashlib
import time
conn = remote('secrecy-vd34kvensehem.shellweplayaga.me',10000)

def time_test():
    start = time.time()
    for _ in range(100):
        conn.recvuntil(b"identity:\n")
        conn.send(("the822441403130014151"  + "\n").encode())
        conn.recvuntil(b"code:\n")
        conn.send(b"098f6bcd4621d373cade4e832627b4f6\n")
    end = time.time()
    print(end - start)
def recursion(string, length):
	global bas
	#print(string)
	if len(string) == length:
		conn.recvuntil(b"identity:\n")
		conn.send(("the" + '\n').encode())
		conn.recvuntil(b"code:\n")
		send = hashlib.md5((bas + string).encode('utf-8')).hexdigest() 
		#print(send)
		conn.send((send + '\n').encode())
		line = conn.recvline()
		#print(line)
		if b'Invalid padding\n' != line and b'Invalid decrypt block\n' != line:
			print(line)
			print(bas + string)
			print(send)
			bas = bas + string
			return string
		return
	for i in range(97, 122):
		recursion(string + chr(i), length)

initial = conn.recvuntil(b"please: ") 
conn.send(b"ticket{MastDock659n22:MNV6Uh8Q5thTQBJVeD6dv4s7T2eAS54WabM-XyCxuYr4Hqee}\n")
global bas
bas = "acpajsavs"
string = recursion("", 3)
print(string)
#time_test()
conn.close()