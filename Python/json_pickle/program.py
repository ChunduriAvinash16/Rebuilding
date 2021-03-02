#write a program to write a list into a file

a=[1,2,3,4,5,6]
''' error typeerror
file=open("list.txt","w")
file.write(a)
file.close()
'''

import json as j
'''original={"Name":"Avinash","Reg_no":321710306006,"College":"GITAM"}
file=open("list.txt","a")
file.write(j.dumps(original))
file.close()'''
'''
file=open("list.txt","a")
file.write("\nHello good morning")
file.close()
'''
file=open("list.txt","r")
j.loads(file.read())
print(file.read())
file.close()