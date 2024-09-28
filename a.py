a = ord(input("Enter the letter:"))
if a >= 65 and a <= 90:
    print(chr(a), "is a Uppercase letter and it's ASCII value is", a)
elif 97 <= a <= 122:
    print(chr(a), "is s Lowercase letter and it's ASCII value is", a)
elif 48 <= a <= 57:
    print(chr(a), "is a number and it's ASCII value is", a)
else:
    print(chr(a), "is a Symbol and it's ASCII value is", a)
