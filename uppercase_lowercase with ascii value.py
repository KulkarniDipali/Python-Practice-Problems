a=ord(input("Enter the letter:"))
if a>=65 and a<=90:
    print(chr(a),"is a Uppercase letter and it's ASCII value",a)
elif a>=97 and a<=122:
    print(chr(a),"is s Lowercase letter and it's ASCII value",a)
elif a>=48 and a<=57:
    print(chr(a),"is a number and it's ASCII value",a)
else:
    print(chr(a),"is a Symbol and it's ASCII value",a)
