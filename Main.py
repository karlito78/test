
for i in range(1, 10):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(2, i+1):
        print(i - j+1, end=" ")
    print()
