from math import sqrt
print("Quadratic Equation: ax^2 + bx + c")

a=int(input("Enter a real number a that is not equal to 0"))
b=int(input("Enter a real number b"))
c=int(input("Enter a real number c"))

def quadratic(a, b, c):
    r= (b * b ) - (4 * a *c)
    print(r)

    if r>0:
        num_roots=2
        result= ((-b )+ (sqrt(r)))/ 2 * a
        result1=((-b) - ((sqrt(r)))) / 2 * a 
        print("The quadratic equation is:" + str(result))
        print("and :" + str(result1))

    elif r==0:
        num_roots=1
        result= (- b) /2 * a
        print("The quadratic equation is:" + str(result))
    else:
        print("No roots, discriminant < 0.")

quadratic(a,b,c)
