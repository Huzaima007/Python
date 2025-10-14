# OOP In Python  
# oop sf object oriented programming 




# Class And Object In Python


# class Student:
#     name = "Huzaima"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)




# class Car:
#     color = "Red"
#     brand = "BMW"

# car1 = Car()
# print(car1.color,car1.brand)
    

# INIT FUNCTION 

# Constructor 
# VERSION 1 
# class Student:
# parameterized constructors 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

# s1 = Student("HUZAIMA" , 100)
# print(s1.name, s1.marks)

# s2 = Student("KARAN" , 90)
# print(s2.name, s2.marks)


# VERSION 2 


# class Student:
#     # default constructor 
#     def __init__(self):
#         pass

# s1 = Student("HUZAIMA" , 100)
# print(s1.name, s1.marks)

# s2 = Student("KARAN" , 90)
# print(s2.name, s2.marks)



# CLASS & INSTANCE ATTRIBUTES 


# class Student:

#     college_name = "ABC"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

# s1 = Student("HUZAIMA" , 100)
# print(s1.name, s1.marks)

# s2 = Student("KARAN" , 90)
# print(s2.name, s2.marks)

# print(Student.college_name)












# class Student:

#     college_name = "ABC"
#     name = "anonymous"


#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

# s1 = Student("HUZAIMA" , 100)
# print(s1.name)






# METHODS 


class Student:

    college_name = "ABC"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def welcome(self):
        print("Welcome Student", self.name)

        

s1 = Student("HUZAIMA" , 100)
s1.welcome()

