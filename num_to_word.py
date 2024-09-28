a=('zero','one','two','three','four','five','six','seven','eight','nine')
b=[]
n=int(input("Enter a number:"))
while n>0:
    r=a[n%10]
    n=int(n/10)
    b.append(r)
    
b.reverse()
print(b)
