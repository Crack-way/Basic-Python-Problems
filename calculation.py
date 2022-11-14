a=int(input("Enter a cost price"))
b=int(input("Enter a selling price"))

def calculation(a,b):
    if(a <b):
        profit=b - a
        print("The profit price is Rs"+str(profit))
    else:
        loss=a - b
        print("The loss price is Rs" + str(loss))

        
calculation(a,b)