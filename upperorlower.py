a=input("Enter a character")

for r in a:  
  r=ord(r)

if(r>= 97 and r<=122):
    print("Lower case alphabet")

elif(r>=65 and r<=90):
    print("Upper case alphabet")