n=int(input("Enter the rows:"))
for i in range(n,0,-2):
  for j in range(0,n-i):
      print(end=" ")
  for j in range(1,i):
      print(j%2," ",end="")
  print()
