import timeit

l=list(range(1000000))
print("----Using enumerate---")
start=timeit.timeit()
for i,ele in enumerate(l):
    pass
end=timeit.timeit()
print(end-start)


start=timeit.timeit()
print("---Using range---")
for i in range(len(l)):
    pass
end=timeit.timeit()
print(end-start)


print("----Using iterobject---")
start=timeit.timeit()
it=iter(l)
for i in range(len(l)):
    pass
end=timeit.timeit()
print(end-start)