n=int(input("Enter a number:"))
a=0
b=1
i=0
while i<=n:
    print(a,end=",")
    c=a+b
    a=b
    b=c
    i=i+1
print(c)
