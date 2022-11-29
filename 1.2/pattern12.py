
n= int(input("Enter the limit : "))
s = 0
d = 0
for i in range(1,n+1):
    s = s * 10 + i
    if i == 1:
        d = 1
    else:
        d = i * (10**(i-1)) + d
    print(str(s)," "* abs((n*2)-(i*2)),str(d))