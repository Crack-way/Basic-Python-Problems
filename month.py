month=int(input('Enter a month number'))

if(month == 1 or month==3 ):
    print("The number of day is 31 days")
elif(month==4 or month==6 or month==9 or month==11):
    print("The number of day is 30 days")
else:
    print("The number of days is 29 days")
