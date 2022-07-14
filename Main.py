for i in range(10):
    # Print leading spaces
    for j in range(1, 10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
for i in range(1, 9):
    for j in range(i):
        print(" ", end=" ")
    for j in range(0, 9 - i):
        print( j+1, end=" ")
        # Count down
    for j in range(8-i,0, -1):
        print(j, end=" ")
        # Next row

    print()