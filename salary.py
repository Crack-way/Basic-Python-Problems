def grossSalary(hoursworked, wage):

   if hoursworked> 40:
    a=hoursworked - 40
    return  a * wage + a * (1.5 * 100) 

   else:
     return wage * hoursworked

hoursworked=int(input("Enter the hours worked"))
wage=int(input("Enter wage amount per hour"))
print(grossSalary(hoursworked,wage))