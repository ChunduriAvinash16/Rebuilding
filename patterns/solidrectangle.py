
n=int(input())
for i in range(3):
    for j in range(n):
        if i==0 or i==2 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()