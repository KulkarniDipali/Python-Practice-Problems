#2:Write a program to convert bits to Megabytes,Gigabytes and Terabytes.
bit=int(input("bits="))
mb=bit/(8*1024*1024)
gb=bit/(8*1024*1024*1024)
tb=bit/(8*1024*1024*1024*1024)
print("megabyte=",mb)
print("gigabyte=",gb)
print("terabyte=",tb)
