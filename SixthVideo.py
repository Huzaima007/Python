#  Functions In Python 

#  method 1 
# def addition(a, b):
#     sum = a + b
#     print(sum)
#     return(sum)

# addition(5, 10)
# addition(2, 10)
# addition(12, 17)

 
#  method 2 

# def addition(a, b):
#     return a + b

# sum = addition(int(input("enter some num")),int(input("enter one more num")))
# print(sum)



# average of 3 numbers 

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(111, 222, 333)


# Types Of function  

# Built-in Functions 

# print("Huzaima") 

# len()

# range()

# type()


# User-defined Functions 
 


# Practice Ques

# Q1

# cities = ["karachi" , "Lahore", "Quetta"]
# heros = ["hulk" , "fireman", "waterman", "windman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heros)



# Q2


# cities = ["karachi" , "Lahore", "Quetta"]
# heros = ["hulk" , "fireman", "waterman", "windman"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(heros)
# print_list(cities)



# Q3 



# n = 5


# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i 
#     print(fact)

# cal_fact(6)    



# Q4


# def converter(usd_val):
#     rs_val = usd_val * 320
#     print(usd_val, "USD =", rs_val, "RS")

# converter(int(input("Add your Ammount")))




# Recursion In Python


# Recursive Function 
# def show(n):
    # if(n == 0): base case
#         return
#     print(n)
#     show(n-1)

# show(10)
