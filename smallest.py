a=int(input("Enter a number A"))
b=int(input("Enter a number B"))
c=int(input("Enter a number c"))

if(a>b and b>c):
    print("c is the smallest number")

elif(b>a and a>c):
    print("c is the smallest number")

elif(c>a and a > b):
    print("b is the largest number")

else:
    print("What")