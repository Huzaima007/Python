# Loops In Python 

# while Loop 
# count = 1
# while count <= 5 : 
#     print("hello")
#     count += 1
    
    
# count = 5
# while count >= 1 : 
#     print("hello")
#     count -= 1

# Practice While Loop 

# Q1 

# count = 1
# while count <= 100 : 
#     print("hello",count)
#     count += 1


# Q2 

# count = 100
# while count >= 1 : 
#     print("hello", count)
#     count -= 1


# Q3 

# mul = int(input("enter a number"))
# i = 1 
# while i <= 10 :
#     print(mul*i)
#     i += 1


# Q4 

# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# Q5 

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx" , i)
#     else:
#         print("finding....")    
#     i += 1    



# Break And continue In while loop 


# Break : used to terminate the loop when encountered 

# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration 


# EX 1 Break

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
    
# print("loop break")


# EX 2 Break
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx" , i)
#         break
#     else:
#         print("finding....")    
#     i += 1    
# print("end of loop")



# EX 3  Continue


# i = 0
# while i <= 5 :
#     if(i == 3):
#         i += 1
#         continue  # skip
#     print(i)
#     i += 1



# For Loops In Python



# list = [1,2,3,4,5,6]

# for val in list:
#     print(list)




# tup = (1,2,3,4,5)

# for num in tup:
#     print(num)




# str = "Huzaima"

# for char in str:
#     print(char)



# for loop with else 


# str = "Huzaima"

# for char in str:
#     print(char)
# else:
#     print("end")    




# str = "Huzaima"

# for char in str:
#     if(char == "m"):
#         print("m found")
#         break
#     print(char)
# else:
#     print("end")    





# Practice 

# Q1 

# list = [1,4,9,16,25,36,49,64,81,100]

# for val in list:
#     print(val)



# Q2 

# list = [1,4,9,16,25,36,49,64,81,100,49]
# x = 49

# idx = 0 
# for val in list:
#     if(val == x):
#         print("num found at idx" , idx)
#     idx += 1    





# Range Function 


# seq = range(10)

# for i in range(10):  //range(stop)
#     print(i)





# for i in range(2,10):  //range(start, stop)
#     print(i)


    

# for i in range(2, 10, 2):  #//range(start,stop,step)
#     print(i)







# for i in range(2, 101, 2):  
#     print(i)







#   Practice


# Ques 1 

# for i in range(1, 101):  
#     print(i)



# Ques 2 

# for i in range(100, 0, -1):  
#     print(i)




# Ques 3 


# n = int(input("enter a number"))

# for i in range(1, 11):
#     print(n * i)





# Pass Statement 


# for i in range(101):
#     pass

# print("some useful work")






# for i in range(101):
#     pass


# if i > 5:
#     pass

# print("some useful work")



# Practice 


# Ques 1  


# Using While loop 
# n = 5 
# sum = 0
# i = 1
# while i <= n:
#     sum += i 
#     i += 1
# print("total sum =", sum)



# Using For loop 

# n = 5 
# sum = 0

# for i in range( 1,n + 1):
#     sum  += i

# print("total sum =", sum)




# Ques 2 

# Using While loop 
# n = 5 
# fact = 1
# i = 1
# while i <= n:
#     fact *= i 
#     i += 1
# print("factorial =", fact)



# Using For loop 
# n = 5 
# fact = 1

# for i in range(1, n+1):
#     fact *= i 
# print("factorial =", fact)

