lis = []
n = int (input("Enter number os elements:"))
for i in range (n):
    lis.append(int(input()))
    lis = list(set(lis))
    lis.sort()
    print("Sorted list:",lis)
