a=int(input("Enter a number A"))
b=int(input("Enter a number B"))
c=int(input("Enter a number C"))

def areaOfTriangle(a,b,c):
    semi=a+b+c/2
    result=(semi*(semi-a) * (semi-b) * (semi-c) ) * 0.5
    print(" The area of Triangle is " + str(result))

areaOfTriangle(a,b,c) 