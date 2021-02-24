l=[{i:i*i} for i in range(10)]
print(l)


l1=[(x,y) for x in (10,20,30) for y in (20,30,40) if x!=y]
print(l1)