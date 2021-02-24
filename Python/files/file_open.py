file=open("hello.txt",mode="a+")
file.write("what is Version control system")
file.close()
print(file.closed)
file=open("hello.txt",mode="r+")
for line in file:
    print(line)
