print("By elif Statement..")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a,"is greatest number")
elif b>a and b>c:
    print(b,"is greatest number")
elif c>a and c>b:
    print(c,"is greatest number")
else :
    print("All numbers are equal")
