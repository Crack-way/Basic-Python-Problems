a=int(input("Enter a day number"))

def day(a):
    if(a%7==0):
        print("Saturday")
    elif(a%7==6):
        print("Friday")
    elif(a%7==5):
        print("Thursday")
    elif(a%7==4):
        print("Wednesday")
    elif(a%7==3):
        print("Tuesday")
    elif(a%7==2):
        print("Monday")
    elif(a%7==1):
        print("Sunday")
day(a)
