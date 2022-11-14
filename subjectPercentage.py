math=int(input("Enter the marks of the math"))
psychology=int(input("Enter the marks of the psychology"))
tourism=int(input("Enter the marks of the tourism"))
python=int(input("Enter the marks of the python"))
java=int(input("Enter the marks of the java"))

def percentage(math,psychology,tourism,python,java):
    result= ((math  + psychology  + tourism + python  + java )/500 ) * 100

    return result 

print("The percentage of the total subject is"+ str(percentage(math,psychology,tourism,python,java)))