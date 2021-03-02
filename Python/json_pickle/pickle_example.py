import pickle
n=int(input())
d={}
for i in range(n):
    key=input("Enter key : ")
    value=input("Enter value : ")
    d[key]=value
f=open("data.pkl","wb")
pickle.dump(d,f)
print("Inserted")
f.close()


f=open("data.pkl","rb")
data=pickle.load(f)
print(data)
f.close()
