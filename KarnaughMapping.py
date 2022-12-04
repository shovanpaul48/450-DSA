def TakeValue(temp,i,j):
    val = int(input("Enter value for " + str(i) + str(j) +" position :"))
    if val == 0 or val == 1:
        temp.append(val)
        return
    else:
        TakeValue(temp,i,j)

def createArray(r,c):

    array2D = []
    for i in range(r):
        temp = []
        for j in range(c):
            val = int(input("Enter value for " +str(i) + str(j)+" position :"))
            if val == 0 or val == 1:
                temp.append(val)
            else:
                TakeValue(temp,i,j)

        array2D.append(temp)
    
    for array in array2D:
        print(array)

    findGroup(array2D)


def findGroup(array2D,r,c):
    count = 0
    for i in range(r):
        for j in range(c):
            if array2D[i][j] == 1:
                if array2D[i+1][j] == 1:
                    count = count + 1
                    if array2D[i][j+1] == 1:
                        






 

def getRowColoumn():
    r = int(input("Enter the number of row : "))
    c = int(input("Enter the number of column :"))
    if  (r == 3 and c == 3 ) or (r == 1 and c==1):
        print("Row and column cant be 3 and 3")
        getRowColoumn()
    else:
        createArray(r,c)
    

if __name__ == '__main__':
   getRowColoumn()
    





