a=int(input("Enter a side of the triangle"))
b=int(input("Enter a side of the triangle"))
c=int(input("Enter a side of the triangle"))

def verifyTriangle(a,b,c):
    if(a and b and c >0):
        print("Side of the triangle is valid")
    
verifyTriangle(a,b,c)