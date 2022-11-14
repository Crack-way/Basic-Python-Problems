name=input("Enter your name")
a=[]
b=[]

for i in name:
   
    if(i!=''):
       a=[i]
       print(a)
    elif(i==' '):
       b=[i]
       print(b)
    
    if(i!= ''):
      result= a[0]
      print(result) 
    else:
      result=a[0] + b[0]
      print(result) 

    




