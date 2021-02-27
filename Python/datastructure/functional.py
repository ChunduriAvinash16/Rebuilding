def check(x):
    if x%2==0:
        return 1
evens=list(filter(check,range(2,25)))
print(evens)