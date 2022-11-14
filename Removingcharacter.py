
a= "Rupesh"
n=int(input("Enter a index to delete char from"))
count=0
myList=[] 
def removeChars(a , n):
    for character in a:
       print(character)
       count= 1 + count
       myList=[ord(character)]
       
    for index , i in enumerate(myList,start=1):
        if(i==n): continue
        a= myList.join(' ') 
        return a 
    
    

    
   

removeChars(a , 0)



    


