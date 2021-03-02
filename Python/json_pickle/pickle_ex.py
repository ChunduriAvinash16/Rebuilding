import pickle
'''f=open("demo.pkl","ab")
data=[12,23,45,"Hello",[12,34,5]]
pickle.dump(data,f)
print("Data return")
f.close()'''


f=open("demo.pkl","rb")
data=pickle.load(f)
print(data)
f.close()
