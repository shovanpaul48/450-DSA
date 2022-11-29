n= int(input("Enter the limit : "))
for i in range(1,n+1):
    if i %2 != 0 and i == 1:
        for j in range (1,i):
            print("1",end="")

    elif i %2 != 0:
        for j in range (1,i):
            print("1",end="")
            if j < i-1:
                j=j+1
                print("0",end="")
                
    elif i%2 ==0:
        for j in range (1,i):
            print("0",end="")
    
            if j < i-1:
                j=j+1
                print("1",end="")
                
    print()
