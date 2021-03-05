n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="") if j<=i  else print(" ",end=" ")
    print()