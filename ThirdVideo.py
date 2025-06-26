# Lists in PY / Array

# marks = [90.5,80.5,70.5,60.5]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])

# student = ["bazan",94.44,11,"karachi"]
# print(student)


# Difference b/w strings and lists in python 
# mutable maens the thing that can be change
# immutable maens the thing that can not be change
# strings are immutable
# lists are mutable

# in this the h of the hello can not be change into y
# str = "hello"
# print(str[0])
# str[0] = "y"


# in this the name can be change from bazan to huzaima
# student = ["bazan",94.44,11,"karachi"]
# student[0] = "huzaima"
# print(student)

# is me jo ha jitni range ha us ma hi hum access kr sakte hain 5 ma ye error dede ga 
# student = ["bazan",94.44,11,"karachi"]
# print(student[5])


# list slicing

# positive slicing
# marks = [90.5,80.5,70.5,60.5]
# print(marks[1:3])
 
# negative slicing 
# marks = [90.5,80.5,70.5,60.5]
# print(marks[-3:-1])

# list method 

# list = [1,2,3]
# Append Method Is Also Called Mutating In The List 
# Append Method / adds one element at the end
# list.append(4)
# print(list)

# Sort Method Are In two Type Ascending And Descending Order

# Ascending Sort Method 
# print(list.sort())
# print(list)

# Descending Sort Method
# print(list.sort(reverse=True))
# print(list)

# Reversed Method / reveses list
# list.reverse()
# print(list)

# Insert Method / insert element at index
# list.insert(2,5)
# print(list)

# Remove Method / removes first occurrence of element
# list.remove(1)
# print(list)

# Pop Method / removes element at index 
# list.pop(2)



# Tuples In Python 

# difference b/w tuple and in list, list are mutable ,tuples are immutable 


# tup = (1,2,3,4,5,6)
# print(type(tup))
# print(tup[0])
# print(tup[1])


# Empty tuple
# tup = ()
# print(tup)
# print(type(tup))


# Single Value tuple
# tup = (1,)
# print(tup)
# print(type(tup))



# Slicing In Tuple 
# tup = (1,2,3,4,5,6)
# print(tup[1:3])


# Tuple Methods 

# tup = (1,2,3,4,5,6)

# Index Method / return index of first occurrence
# print(tup.index(2))

# Count Method / count total ocurences
# print(tup.count(2))


# Practice Ques

# Q1
# sol 1
# movies = []
# movie1 = input("Enter Movie 1")
# movie2 = input("Enter Movie 2")
# movie3 = input("Enter Movie 3")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# sol 2
# movies = []
# movies.append(input("Enter Movie 1"))
# movies.append(input("Enter Movie 2"))
# movies.append(input("Enter Movie 3"))
# print(movies)



# Q2

# list1 = [1,2,1]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")


# list1 = [1,2,3]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# Q3

# grade = ("C", "D", "A", "A", "B", "B", "A",)
# print(grade.count("A"))

# Q4

# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)