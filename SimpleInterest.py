
principal=int(input("Enter a principal amount"))
time=int(input("Enter a time"))
rate=int(input("Enter a rate"))

def simpleInterest(principal , time , rate):
    result= principal * time * rate / 100
    print(result)

simpleInterest(principal,time,rate)

