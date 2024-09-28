print("By Nested-if Statement..")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b:
    if a>c:
        print(a,"is greatest number")
if b>a:
    if b>c:
        print(b,"is greatest number")
if c>a:
    if c>b:
        print(c,"is greatest number")
else:
    print("All numbers are equal",a,b,c)
