a=int(input("Enter a side of the triangle"))
b=int(input("Enter a side of the triangle"))
c=int(input("Enter a side of the triangle"))

def check(a,b,c):
    if(a==b==c):
        print("It is equilateral triangle")

    elif(a != b != c and c!=a):
        print("It is scalene triangle")

    elif(a==b or a==c or b==c) :
        print("It is isosceles triangle")
    
check(a,b,c)