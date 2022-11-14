a=input("Enter a character")

def checkCharacter(a):
    for r in a:
      result=ord(r)
    if result>=97 and result <=122:
        print("Alphabet")
    
    elif result>=65 and result <=90:
        print("Alphabet")

    elif result>=48 and result <=57:
        print("NUmbers")
    
    else:
        print("Special Characters")
    
checkCharacter(a)