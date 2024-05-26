def floydstriangle(n):
    num = 0
    for i in range(n):
        for j in range(i + 1):
            num += 1
            print(num, end=" ")
        print()

n = int(input("Enter the number of rows for Floyd's Triangle: "))
floydstriangle(n)
