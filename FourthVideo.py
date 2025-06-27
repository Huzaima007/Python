# Dictionary In Python 
# dict are unodered,mutable(changeable),& don't allow duplicate the keys 


# Storing
# dict = {
#     "key" : "Value",
#     "name" : "Huzaima",
#     "learning" : "python",
#     "age" : 16,
#     "is_adult" : "True",
#     "marks" : 33.3,
#     "list" : ["Python", "C", "Java", "Javascript"],
#     "tuple" : ("dictionary", "Set") 
# }
# print(dict)
# print(type(dict))




# Accessing the keys seperately
# dict = {
#     "key" : "Value",
#     "name" : "Huzaima",
#     "learning" : "python",
#     "age" : 16,
#     "is_adult" : "True",
#     "marks" : 33.3,
#     "list" : ["Python", "C", "Java", "Javascript"],
#     "tuple" : ("dictionary", "Set") 
# }

# print(dict["key"])
# print(dict["age"])
# print(dict["is_adult"])






# changing and adding the values of the keys 
# dict = {
#     "key" : "Value",
#     "name" : "Huzaima",
#     "learning" : "python",
#     "age" : 16,
#     "is_adult" : "True",
#     "marks" : 33.3,
#     "list" : ["Python", "C", "Java", "Javascript"],
#     "tuple" : ("dictionary", "Set") 
# }

# dict["name"] = "Bazan"
# dict["surname"] = "Sajid"
# print(dict) 




# empty dictionary

# null_dict = {}
# print(null_dict)





# Assigning the value to the null dictionary 

# null_dict = {}
# null_dict["name"] = "apnacollege"
# print(null_dict)





# Nested dictionary

# student = {
#     "name" : "Bazan Kumar",
#     "subjects" : {
#         "phy" : 99,
#         "chem" : 98,
#         "math" : 97,
#         "eng" : 96,
#     }
# }

# whole student 
# print(student)
# only subjects
# print(student["subjects"])
# only one subject
# print(student["subjects"]["chem"])






# Dictionary Methods 

# key method / return all keys
# student = {
#     "name" : "Bazan Kumar",
#     "subjects" : {
#         "phy" : 99,
#         "chem" : 98,
#         "math" : 97,
#         "eng" : 96,
#     }
# }

# print(student.keys())
# typecast in list 
# print(list(student.keys()))
# finding the total number of keys
# print(len(student))
# print both in one line 
# print(len(list(student.keys())))


 
# Values Method / return all values

# student = {
#     "name" : "Bazan Kumar",
#     "subjects" : {
#         "phy" : 99,
#         "chem" : 98,
#         "math" : 97,
#         "eng" : 96,
#     }
# }

# print(student.values())



# Items method / return all (key,val) pairs as tuples 

# student = {
#     "name" : "Bazan Kumar",
#     "subjects" : {
#         "phy" : 99,
#         "chem" : 98,
#         "math" : 97,
#         "eng" : 96,
#     }
# }

# print(student.items())



# Get Method / returns the key acc to value 

# student = {
#     "name" : "Bazan Kumar",
#     "subjects" : {
#         "phy" : 99,
#         "chem" : 98,
#         "math" : 97,
#         "eng" : 96,
#     }
# }

# print(student.get("name2")) by method it give value none
# print(student["name2"]) by neutral way its give error 




# Update Method / insert the specified item to the dictionary

# student = {
#     "name" : "Bazan Kumar",
#     "subjects" : {
#         "phy" : 99,
#         "chem" : 98,
#         "math" : 97,
#         "eng" : 96,
#     }
# }

# student.update({"city" : "karachi"})
# print(student)




# Set In Python 
# sets are mutable but element are immutable
# element in the set must be unigue and immutable 
# list and dictionary never be store in the set 
# duplication not allow in set 


# collection = {1,2,3,4}
# print(collection)
# print(type(collection))


# to write empty set we have to write
# collection = set()
# print(type(collection))
 
 
 
#  Sets Method 

# Add method / adds an element
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(3)
# print(collection)


# Remove Method / removes an element 
# collection = {1, 2, 3, 4, 5}
# collection.remove(3)
# print(collection)


# Clear Method / empties the set 
# collection = {1, 2, 3, 4, 5}
# collection.clear()
# print(collection)


# Pop Method / removes a random value 

# collection = {"hello", "Huzaima", "Bazan", "Python"}
# collection.pop()
# print(collection)


# Union Method / combine both set values and return new 

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))


# Intersection Method / combines common values and return new 

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.intersection(set2))




# Practice Question 

# Q1 
# dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", " list of facts and figures"]
# }

# print(dict)


# Q2 
# subjects = {
#     "python", "java" , "c++" , "python", "js", "java", "python", "java", "c++", "c"
# }

# print(len(subjects))


# Q3  

# marks = {}

# x = int(input("phy"))
# marks.update({"phy" : x})

# x = int(input("chem"))
# marks.update({"chem" : x})

# x = int(input("math"))
# marks.update({"math" : x})

# print(marks)


# Q4

# values = {("float",9.0),("int",9)}
# print(values)
