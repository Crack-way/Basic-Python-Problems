a=int(input("Enter a number A"))
b=int(input("Enter a number B"))
c=int(input("Enter a number C"))
print (a)
print(b)

if((a>b) and (b>c)):
    print("A is the largest number") 
elif((b>a) and (a>c)):
    print("B is the largest number")
elif((c>a) and (a > b)):
    print("C is the largest number")
else:
    print("What")