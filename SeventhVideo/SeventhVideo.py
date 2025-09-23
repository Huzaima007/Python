# File Input/Output In Python 






# READ ONLY METHOD

# IT READS WHOLE FILE 


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



# IT ONLY READS ONE LINE 

# READ ONLY LINE 1 


# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r")
# line1 = f.readline()
# print(line1)
# f.close()


# READ ONLY LINE 2

# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()




# WRITE ONLY METHOD 



# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "w")

# f.write("")
# f.close()



# WRITE AND READ METHOD 


# f = open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r+")

# f.write("aaa")
# f.close()


# WITH SYNTAX 

with open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r") as f:
    data = f.read()
    print(data)


with open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "w") as f:
    f.write("new data ")



# DELETING A FILE 