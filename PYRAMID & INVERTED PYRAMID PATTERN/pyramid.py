size = int(input("Enter the size of the pyramid: "))

for i in range(size):
    for j in range(size,i+1,-1):
        print(" ", end="")
        
    for k in range(2*(i-1)+3):
        print("*", end="")
        
    print()
        