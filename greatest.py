a=int(input("Enter a number A"))
b=int(input("Enter a number B"))
c=int(input("Enter a number C"))

def largest(a, b,c):
    if(a > b and b > c):
        print(str(a)+ " is the largest number")
    elif(b > a and a >c):  
        print(str(b)+ " is the largest number")
    elif(c > b and b >a):
        print(str(c)+ " is the largest number") 
    elif(a==b and c< a):
        print("A and b are greater but both are equal")
    elif(a==c and b< a):
        print("A and C are greater but equal")
    elif(c==b and c< a):
        print("c and b are greater but both are equal")
    else:
        print("All are equal")
largest(a,b,c)
