num=int(input("Enter a number(having more than two digits):"))
reverse=0
while(num>0):
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
print("Reversed number is:",reverse)
