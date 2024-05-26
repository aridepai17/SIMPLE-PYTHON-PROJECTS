size = int(input("Enter the size of the pyramid: "))

for i in range(size-1):
    for j in range(i):
        print(" ", end="")
        
    for k in range((size-i)*2-3):
        print("*", end="")
    
    print()