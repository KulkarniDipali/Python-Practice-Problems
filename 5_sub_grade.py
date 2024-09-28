pwp=int(input("PWP marks="))
mgt=int(input("MGT marks="))
mad=int(input("MAD marks="))
eti=int(input("ETI marks="))
php=int(input("PHP marks="))
avg=(pwp+mgt+mad+eti+php)/5
print("Average=",avg)
if avg>=90 and avg<=100:
   print("You got A grade")
   if avg>=80 and avg<90:
      print("You got B grade")
      if avg>=70 and avg<80:
         print("You got C grade")
         if avg>=60 and avg<50:
            print("You got D grade")
            if avg>=500 and avg<40:
              print("You got E grade")
else:
    print("You are fail")
