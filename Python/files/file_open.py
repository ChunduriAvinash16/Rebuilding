'''
File Handling:
    Reading  data from file and writing data into file is called File Handling or file programming
    1) The major use of file handling is we can store the data or information permenantly
    2)If we want to perform file handling , there are some methods and modes of operations that we have to follow
    3)Modes of File Handling are
        1)w ------ write mode 
        2)r--------read mode
        3)a--------append mode
        4)rb-------read binary
        5)wb-------write binary
    4)Methods of File handling
        1)open()
        2)write()
        3)read()
        4)close()
    open():It id used to open a file in a specified location
        syntax:
            file_obj=open("filename.extension","mode of operation")
            return type of open() function is an file_obj address 
            default mode is read mode
    read():In is used to readt the data present in te file.
'''


'''while creating a file through the program the mode of operation should be w'''
'''file=open("hello2.txt","a")
data="\nWhat is the food?"
file.write(data)
file.close()
'''
file=open("hello.txt","r")
data=file.read()
print(data)
file.close()
