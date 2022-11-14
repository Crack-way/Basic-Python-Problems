pi=22/7
radius=int(input("Enter a radius."))

def areaOfCircle(pi, radius):
    result= pi * (radius * radius)
    print(result)

areaOfCircle(pi,radius)

def circumference(radius):
    result= 2 * pi * radius
    print(result)

circumference(radius)