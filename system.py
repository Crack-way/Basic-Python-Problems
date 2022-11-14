display=""" WELCOME TO SUNWAY CHARACTER CHECK SYSTEM MAITIDEVI, KATHMANDU"""
print(display)

d1= """ Enter 1 to check how many uppercase letter"""
d2= """ Enter 2 to check how many lower letter"""
d3= """ Enter 3 to check how many numeric in string"""
d4= """ Enter 4 to check how many special Character"""
d5= """ Enter 5 to check how many uppercase letter"""
a=input("Enter a string")

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
num=int(input("Enter your choice"))

count=0
def checkLowerCase(a):
    arr =list(a.strip("  ")) 
    print(arr)
    for check in arr:
        p=ord(check)
        if p >=97 and p <=120:
           count = 1 + count
    return count
      
    
def checkUpperCase(a):
    for r in a:
      result=ord(r)
    for check in result:
     if check>=65 and check<=90:
        count +=1
        return count
     

def checkNumbers(a):
    for r in a:
      result=ord(r)
      
    for check in result:
     if check>=48 and result <=57:
        count +=1
        return count

if(count==1):
    checkUpperCase(a)
    print("The number of upper case letter is" + str(count))
elif(count==2):
    checkLowerCase(a)
    print("The number of lower case letter in string is"+ str(count))
    
        

