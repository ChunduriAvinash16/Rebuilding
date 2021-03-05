n=int(input())
px=n-1
py=n-1
for i in range(n):
    for j in range((n-1)*2+1):
        if i==n-1:
            print("*",end="")
            continue
        if px==j or py==j:
            print("*",end="")
        else:
            print(" ",end="")
    px-=1
    py+=1
    print()