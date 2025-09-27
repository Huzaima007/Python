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

# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "r") as f:
#     data = f.read()
#     print(data)


# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\demo.txt", "w") as f:
#     f.write("new data ")



# DELETING A FILE 

# import os

# os.remove("File name")




# PRACTICE QUESTIONS 



# QUES 1


# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "w") as f:
#     f.write("SAB BOLO HI\n")
#     f.write("TUM SAB BOLO BYE")




# QUES 2 


# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("SAB", "HUM")
# print(new_data)

# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "w") as f:
#     f.write(new_data)




# QUES 3 

# word = "BOLO"
# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("not found")






# Wrap Ques 3 In A Function 


# def check_for_word():
#     word = "BOLO"
#     with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#            print("Found")
#         else:
#             print("not found")

# check_for_word()






# QUES 4  


# def check_for_line():
#     word = "BOLO"
#     data = True
#     line_no = 1
#     with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1

# check_for_line()




# QUES 5 



#  METHOD 1 


# with open("G:\HUZAIMA_WORK\Python\SeventhVideo\practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]


#  METHOD 2 

# count = 0
# with open("SeventhVideo\practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

# print(count)