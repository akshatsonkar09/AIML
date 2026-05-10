# #PRIME NUMBERS BETWEEN RANGE#
# a = 30 
# b = 60

# for num in range(a,b+1):
#     for i in range(2,num):
#         if num%i == 0:
#             break

#     else:
#         print(num, end=" ")




# import numpy as np

# arr = np.array([1,0,3,2])
# arr = np.sort(arr)
# arr = arr[::-1]
# print(arr)



# arr = np.sort(np.array([1, 0, 3, 2]))[::-1]     #This happens because of bodmas/Precedence rule
# print(arr)





# a, b = 0, 1 
# print("Fibonacci Series:") 
# for i in range(0,100): 
#     print(a, end=" ") 
#     a, b = b, a + b


# def gcd(a,b):
#     while (b!=0):
#         a,b=b,a%b
#     return a

# def lcm(a,b):
#     value = (a*b)//gcd(a,b)
#     return value

# print(lcm(4,8))




# num = int(input("Enter a number: ")) 
# order = len(str(num)) 
# sum = 0 
# temp = num 
# while temp > 0: 
#     digit = temp % 10 
#     sum += digit ** order 
#     temp //= 10 
# if num == sum: 
#     print(num, "is an Armstrong number") 
# else: 
#     print(num, "is not an Armstrong number") 









# tuple = (1, 2, 3) 
# tuple = tuple + (4,)    
# print("Tuple after adding:", tuple) 
# print("Length of tupple:", len(tuple)) 
# print("Check 2 in tuple:", 2 in tuple) 
# print("Access item at index 1:", tuple[1]) 


# # f = True  
# # g = False

# g = 7
# f = 8


# print("f and g:", f and g)  
# print("f or g:", f or g)  
# print("Not f:", not f) 




# p = 7
# q = 8

# print("Bitwise AND :", p & q)
# print("Bitwise OR :", p | q)
# print("Bitwise XOR :", p ^ q)
# print("Bitwise Complement :", ~p)
# print("Left Shift :", p << 1)
# print("Right Shift :", p >> 1)


# str1 = "Hello"  
# str2 = "World"  
# result = str1 + " " +str2  
# print("String which is concantenated:", result)  
# print("First character:", result[0])  
# print("Last character using negative value:", result[-1])  
# print("Substring [0:5] which means 0 to 5:", result[5:0:-1])
# # print("Substring [0:5] which means 0 to 5:", result[0:5:-1])    Returns empty string
# print("Substring [5:] which means 6 to End:", result[5:])