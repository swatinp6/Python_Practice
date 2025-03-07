a=int(input("Enter a number: "))
if(a>1):
    for x in range(2,a):
        if(a%x==0):
            print("not a prime number")
            break
    else:
        print("prime number")
        
else:
    print("lesser than 1")