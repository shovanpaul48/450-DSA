for i in range(1,5):
    k=i
    if i == 1:
        print(k,end="")
    else:
        for j in range(1,i):
            k = k +1
            print(k, end="")
    print()