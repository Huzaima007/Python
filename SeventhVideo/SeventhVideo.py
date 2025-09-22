# File Input/Output In Python 






# READ ONLY METHOD


# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()




# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r")
# data = f.read(6)
# print(data)
# print(type(data))
# f.close()





# READ ONLY LINE 1 


# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r")
# line1 = f.readline()
# print(line1)
# f.close()


# READ ONLY LINE 2

f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close()
