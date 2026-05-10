
print("Hello World")







#Reversing And printing list#

lst = [1,2,3,4]
# print(lst.reverse())        #reversing the list but not returning Hence NONE


lst = [1,2,3,4]
#Original List lost
lst.reverse()
print(lst)


#Reversed List is stored as a copy
lst = [1,2,3,4]
reverse = list(reversed(lst))
print(reverse)
print(lst)

#Reversing And printing list#


print("\n\n")






a = 10
b = 10.5
c = "Akshat"
d = [1,2,3]
e = (1,2,3)
f = {1,2,3}
g = {"harry" : 5}


#FINDING DATATYPE OF A VARIABLE#


print("Type of a which is" ,a, "is", type(a))
print("Type of b which is",b, "is",type(b))
print("Type of c which is" ,c, "is", type(c))
print("Type of d which is" ,d, "is", type(d))
print("Type of e which is" ,e, "is", type(e))
print("Type of f which is" ,f, "is", type(f))
print("Type of f which is" ,g, "is", type(g))


#FINDING DATATYPE OF A VARIABLE#


print("\n\n")


# name = input("Enter Your name")
# # name = input()        Basic form for input By default input is taken as a string

# # num = input(int("Enter Number"))
# num = int(input("Enter Number"))



#ARITHMETIC OPERATIONS

d = 2
e = 7
f = 9.5

print("Addition of number:", d + e)
print("Subtraction of number:", e - d)
print("Multiplication of number:", e*d)
print("Exponential of number:", e**d)       # e to the power d
print("Division of number:", e/d)
print("Floor Division of number:", e//d)    #Only Quotient
print("Addition of number:", e + f)     #Implicit typecasting int into float
print("Addition of number:", e + int(f))    

#string cannot be implicitly typecasted

#ARITHMETIC OPERATIONS


print("\n\n")



#Explicit Typecasting


x = 12
y = 3.7
z = "8"
# print(z + y)   #string cannot be typecasted to float

print("Int to Float:", float(x))        #Explicit Typecasting
print("Float to Int:", int(y))
print("String to Int:", int(z))
print("Int to String:", str(x))
print("Float to String:", str(y))


#Explicit Typecasting



print("\n\n")


# Logical operators

f = True
g = False

print("f and g:", f and g)
print("f or g:", f or g)
print("Not f:", not f)

# Logical operators


print("\n\n")


# Bitwise operators
p = 7  
q = 8   

print("Bitwise AND :", p & q)
print("Bitwise OR :", p | q)
print("Bitwise XOR :", p ^ q)
print("Bitwise Complement :", ~p)




print("Left Shift :", p << 1)
''' 
x = 5;   // binary: 00000101
x << 1;  // result: 00001010 = 10
x << 2;  // result: 00010100 = 20 
'''

print("Right Shift :", p >> 1)
'''
x = 20;   // binary: 00010100
x >> 1;   // result: 00001010 = 10
x >> 2;   // result: 00000101 = 5
'''
# Bitwise operators




print("\n\n")



#STRINGS#

str1 = "hello"
str2 = "world"
# str = 'Hello'/"Hello"/'''Hello''' (All correct)

result = str1 + " " + str2
print("String which is concantenated:", result)

print("Capitalise String", str1.capitalize())
print("Capitalise String", result.capitalize())
print("First character:", result[0])
print("Last character using negative value:", result[-1])
print("Substring using negative value / reverse:", result[::-1])
print("Substring [0:5] which means 0 to 5:", result[0:5])   # 0 to 4 aka Slicing a String
print("Substring [5:] which means 5 to End:", result[5:])
print("Length of string is",len(str1))
print("Number of times l occur:",str1.count('l'))       #Important
print(str1.replace("hello", "Fuck You"))


print("\n\n")

'''
1) Strings are immutable → once a string is created, it cannot be changed in memory.
Example: "hello" will always remain "hello". You can’t change str1[0] = "H" (will throw error).

2) When you do something like:

str1.capitalize()
→ it does not modify str1, but instead creates a new string ("Hello") and returns it.

3) Since the result is a new string object, if you don’t assign it to a variable, it’s lost after that line executes.

str1 = str1.capitalize()   # Now str1 actually changes

'''


'''
1) Whenever you do something like:

str1 = "hello"
print(str1.capitalize())   # "Hello"
print(str1)                # "hello"


👉 The method .capitalize() returned a new string ("Hello"), but str1 itself is still "hello".

2) If you want the change to stick, you must assign it back:

str1 = str1.capitalize()
print(str1)   # "Hello"

'''
#STRINGS#


print("\n\n")


#LIST#


# Lists are mutable

l1 = [7, 9, "harry"]   # list can contain int, str, etc.

# Indexing is possible(like strings)

print("l1[0:2] =", l1[0:2])  # Slicing allowed

l2 = [1, 8, 7, 2, 21, 15]
print("\nOriginal list:", l2)

l2.sort()
print("After sort():", l2)

l2.reverse()
print("After reverse():", l2)

l2.append(8)
print("After append(8):", l2)

l2.insert(3, 4) 
print("After inserting 4 at index 3:", l2)

# popped_value = l2.pop(2)  # removes element at index 2
# print("After pop(2):", l2, "| Popped value:", popped_value) #Important#

l2.pop(2)
print("After pop at index 2:", l2) #Important#

l2.remove(21)  # removes first occurrence of 21
print("After remove(21):", l2)



#LIST#


print("\n\n")



#TUPLES#


# Tuples are immutable sequences
# They are faster and used for fixed collections of items.


a = ()  # empty tuple
print("Empty tuple:", a)

a = (1,)  # tuple with one element requires a trailing comma
print("Single element tuple:", a)

a = (1, 7, 2, 1, 1)  # tuple with multiple elements (with repetition allowed)
print("Tuple a =", a)

a = a + (4,)      #Saved
print("Tuple a after adding 4", a)

# print("Tuple after adding 4:", a+ (4,))     #Not saved
# print("Tuple a =", a)

print("Count of 1 in a:", a.count(1))    # number of times 1 occurs
print("Index of first occurrence of 1:", a.index(1))  # index of first occurrence       IMPORTANT
print("Check 2 in tuple:", 2 in a)      #True or False answer


# Reminder: tuples do NOT have sort, append, remove, etc. because they are immutable.


#TUPLES#




print("\n\n")








#DICTIONARY#

#Dictionary is Mutable, Unordered, Indexed(but cannot use marks[0] type), Cannot contain duplicate keys. 

marks = {   #Forgot to write = 
    "Harry" : 99, "Akshat" : 90,
    'Ravi': 88,
    0 : '''Harry''' #Mistake - Used = instead of :
}
print(marks)
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 95, "Ram": 89})  #updates if already exist and create if not
print(marks)


print(marks.get("Akshat")) #Prints None when wrong
print(marks["Akshat"]) #Gives error when wrong

marks.clear()
print(marks)

marks = {}  #This is an empty dictionary
s = set()   #This is an empty set

#DICTIONARY#


print("\n\n")


#SETS#

#Set can have both int and string but not list

s1 = {1,3,5,6,8,10}
s2 = {2,4,5,8,10}

print("\nOriginal Set:", s1)

print("Length of Set is",len(s1))
s1.add(2)


popped_value = s1.pop()  # Removes arbritary value from set
print("After pop random:", s1, "| Popped value:", popped_value) #Important#

s1.remove(8)  # removes first occurrence of 8
print("After remove(8):", s1)

print("Union",s1.union({8,10}))
print("Union",s1.union(s2))
print("Intersection",s1.intersection(s2))
print("S1 is subset of ",s1.issubset(s2))
print("S2 is superset of S1",s1.issuperset(s2))


#s1 - s2 ie remove value from s1 that are also in s2

#SETS#



print("\n\n")


#Inputing numbers in a list#

n = int(input("How many Numbers you want\n"))
numbers = []

for i in range(n):
    num = int(input(f"Enter {i+1} Number\n"))
    numbers.append(num)

print(numbers)

#Inputing numbers in a list#



print(max(numbers))

print("\n\n")



#Finding word with vowel#
names = ['akshat','ayush','sachin']

for i in names:
    if i[0].lower() in 'aeiou':     # i[0] means take the first letter of each words
        print(i)
#Finding word with vowel#



print("\n\n")


#Reversing a List#
t = (1,2,3,4,5)
reversed = tuple(reversed(t))       #IMPORTANT
print(t)
print(reversed)
#Reversing a List#


print("\n\n")


#Removing even numbers/Printing odd numbers#
num = set(range(1,11))

for i in list(num):
    if i % 2 == 0:
        num.remove(i)

print(num)
#Removing even numbers/Printing odd numbers#

print("\n\n")


#SETS#
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("Set1 is a Subset of Set2")
else:
    print("Set1 is NOT a Subset of Set2")
#SETS#


print("\n\n")

#FUNCTION FOR HCF#
def gcd (a,b):
    while b != 0:
        a,b = b, a%b
    return a
#FUNCTION FOR HCF#


print("\n\n")


#FUNCTION FOR LCM#
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = (a * b) // gcd(a, b)
print("LCM of", a, "and", b, "is", lcm)
#FUNCTION FOR LCM#


print("\n\n")

#PRIME NUMBERS BETWEEN RANGE#
a = 30 
b = 60

for num in range(a,b+1):
    for i in range(2,num):
        if num%i == 0:
            break

    else:
        print(num, end=" ")


# for num in range(a, b + 1):
#     for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#     else:
#             print(num, end=" ")


#PRIME NUMBERS BETWEEN RANGE#



print("\n\n")

#COMPLEX NUMBERS#

a = complex(2, 3)   # 2 + 3j
b = complex(4, -1)  # 4 - 1j

#COMPLEX NUMBERS#


#CONDTIOTIONAL STATEMENTS#

    #If,Elif and Else If#

    #Syntax#
# if (condition1): # if condition1 is True 
#     print ("yes") 
# elif(condition2): # if condition2 is True  
#     print("no") 
# else:             # otherwise 
#     print("maybe")
    #Syntax#

    #If,Elif and Else If#

    #Relational Operators#
        #   ==, >=, <=
    #Relational Operators#
print("\n\n")

    #Logical Operators#
a1 = 23
a2 = 32
a3 = 20 

if (a1 > a2 and a1>a3):
    print(f"a1 = {a1} is greatest")

elif (a2 > a3 and a2>a1):
    print(f"a2 = {a2} is greatest")

else:
    print(f"a3 = {a3} is greatest")
    #Logical Operators#

#CONDTIOTIONAL STATEMENTS#


print("\n\n")


#LOOPS#


#   while (condition): # The block keeps executing until the condition is true 

i = 0 
while i < 5: # print "Harry" – 5 times! 
    print("Harry")     
    i = i + 1   #i++ is invalid in python

#Note - A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

l = [1, 7, 8] 
for item in l: 
    print(item) # prints 1, 7 and 8 

    #Syntax
#range(start, stop, step_size) 

for i in range(0,7): # range(7) can also be used. 
    print(i) # prints 0 to 6

#Note- break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now. 


#Break Statement#
for i in range (0,80): 
    print(i)     # this will print 0,1,2 and 3 
    if i==3:
        break 
#Break Statement#



#Continue Statement#
#‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”. 
for i in range(4): 
    print("printing") 
    if i == 2:   # if i is 2, the iteration is skipped  
        continue 
    print(i) 
#Continue Statement#


#Pass Statement#

#'pass' is a null statement in python. It instructs to “do nothing”
l = [1,7,8] 
for item in l: 
    pass          
# without pass, the program will throw an error
#Pass Statement#


#LOOPS#



print("\n\n")


#LOOP BASIC EXERCISES#

#Exercise 1#
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

#Method-1
n = 5
for i in range(1, n+1):
    print(' '*(n-i) + '* ' * i)

#Method-2
n = 5
for i in range (n+1):
    print(" "*(n-i), end=' ') 
    print("* "*i, end=' ')
    print('')

#Exercise 1#
print("\n\n")

#Exercise 2#
#Important#
n = 5
for i in range(n):
    print((chr(65 + i) + ' ') * (i+1))

#Exercise 2#

print("\n\n")

#LOOP BASIC EXERCISES#

# for i in range(1,11,-1): # Invalid, slicing dont work on for loop






#FUNCTIONS#
# Two types in python: Built in and User defined 
# Examples of built in  len(), print(), range() etc.


def greet(name = "Stranger"):   # When no argument is passed the funtion will run a default value aka stranger
    print("Hello " + name)

print(greet("Akshat"))
print(greet())

'''
Argument is the input that we give to the function for functions with need of input ie argument we call them argument function
    
If the function does not have a return statement then it does not return any value that you can store 

However if it does then you can either call it in a print function where it will be called once and removed the moment after that line is executed OR you can store the value in a variable for future uses
'''

#Functions Examples#

def factorial1(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial1(n-1)

num = 5
print("Factorial:", factorial1(num))


def sum_of_first_natural_numbers (num):
    sum = num
    
    # if (num <= 0):
    #     break     break can only be used in for and while loop
    # if (num <= 0):
    if num <= 0:
        return 0
    
    # OR
    # if num <= 1:
    #     return 1

    else:
        return sum + sum_of_first_natural_numbers(num-1)

print(sum_of_first_natural_numbers(5))
#Functions Examples#
#FUNCTIONS#


print("\n\n")



#FILE I/O OPERATIONS#
'''
There are 2 types of files: 
1. Text files (.txt, .c, etc) 
2. Binary files (.jpg, .dat, etc)

r - open for reading 
w - open for writing  
a - open for appending 
+  - open for updating. 
rb will open for read in binary mode. 
rt will open for read in text mode.

'''

file = open("file.txt","r")     #Opening of file
text = file.read()      #Read the whole file
textbyline = file.readline()        #Read one line from a file
print("This is text = " + text)
print("This is text by line = " + textbyline)
file.close()

file = open("file.txt", "w")
file.write("This is newly written and old is replaced")
file.close()

with open("file.txt","r") as file:  # Open the file in read mode using 'with', which automatically closes the file 
    text = file.read()
    print(text)

#FILE I/O OPERATIONS#


print("\n\n")

'''OOPS'''
class employee:     
    language = "python"      # Specific to Each Class 
    salary = 1200000

# static method is a method to make a function that does not use the self-parameter

#   @staticmethod       Typing this and no need for self
    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    def __init__(self):     #anything with init is gonna be called as soon as it was created and is called dunder method(__method__ type)
        print("This is for an object")




'''
    def getinfo():     #This function is part of employee class 
        print(f"The is language is {language}. The salary is {salary}")

harry.getinfo()    This will say that an argument is given but the function is a no argument function
This is because compiler reads it like 
employee.getinfo(harry) This is wrong as an argument is given
'''
    


harry = employee()   # Object Instatiation 
harry.name = "Harrison"     # Instance Attribute
harry.language = "JAVA"     #Redefing class attribute using instance attribute 
print(harry.name,harry.language, harry.salary)

harry.getinfo()
#employee.getinfo(harry)

# Here name is object attribute whille language and salary are class attribute


'''OOPS END'''


'''INHERITANCE AND OOPS START'''
class employee:     # This is called base class for this topic and old employee class is gone
    salary = 200000
    company = "Microsoft"
    def get_info(self):
        print(f"The name of employee is {self.name} and his salary is {self.salary} and he works in {self.company}.", end=" ")

employee.name = "Akshat"
akshat = employee()
print(akshat.company)
akshat.get_info()
print()     #For new line


class Programmer(employee):     #This is derived class as it has all the objects of employee class as well as its own
    language = "JAVA"
    def show_language(self):
        print(f"The language he uses is {self.language}")

akshat = Programmer()
# print(akshat.get_info(), akshat.show_language())      This will give NONE NONE as there is no return value in function so it prints the things written in functions and then returns NONE
akshat.get_info(), akshat.show_language()



'''
You can use inheritance at multiple levels
Eg-
class employee():
    Objects 1

class Coder():
    Objects 2

class Programmer():
    Objects 3


Now 
    class SingleLevel(employee):
        Objects 1 & 4

    class Multiple(employee,Coder):
        Objects 1,2 & 5

    class MultiLevel(employee):      //Objects 1
        class Level_1(Coder):            //Objects 1 & 2
            class Level_2(Programmer):       //Objects 1,2 & 3
                Objects 1,2,3 & 6

//4,5,6 woh hai jo khud new class/ derived class me banaye hai

'''
'''INHERITANCE AND OOPS END'''



'''SUPER METHOD START'''
class employee():
    a = 1
    def __init__(self):
        print("Constructor of Employee")


class coder(employee):
    b = 2
    def __init__(self):
        print("Constructor of Coder")


class programmer(coder):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    c = 3

o = programmer()
print(o.a, o.b, o.c)    #Without super init only constructor of programmer is gonna print but with it the parents class constructor will also work
'''SUPER METHOD END'''



'''CLASS METHOD, PROPERTY DECORATOR AND SETTER START'''
#IMPORTANT
class employee():
    a = 1
    @classmethod
    def show (self):
        print(f"The class attribute of a is {self.a}")

    @property
    def name(self):
        return f"{self.fname},{self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

o = employee()
o.a = 43

o.name = "Akshat Sonkar"
print(o.fname, o.lname)
o.show()
    #Without class method the value of instance attribute is shown ie 45
'''CLASS METHOD, PROPERTY DECORATOR AND SETTER START'''


'''OPERATOR OVERLOAD START'''
class number:
    def __init__(self,n):
        self.n = n

    #Without this function the code will throw an error
    def __add__(self, num):
        return self.n + num.n

n = number(1)
m = number(2)

print(n + m)

# Without __add__()
# TypeError: unsupported operand type(s) for +: 'number' and 'number'
# Because Python doesn't know how to add two objects of a user-defined class unless you tell it.


'''
p1+p2 # p1.__add__(p2) 
p1-p2 # p1.__sub__(p2) 
p1*p2 # p1.__mul__(p2) 
p1/p2 # p1.__truediv__(p2) 
p1//p2 # p1.__floordiv__(p2)  
__str__() # used to set what gets displayed upon calling str(obj) 
__len__() # used to set what gets displayed upon calling.__len__() or 
len(obj) 
'''

'''OPERATOR OVERLOAD END'''








#WEAK#

s = "He!!o Wo@rld 123"
result = "".join(ch for ch in s if ch.isalpha())
print("Original:", s)
print("Only alphabets:", result)




result_list = []
for ch in s:                # go through each character in the string
    if ch.isalpha():        # keep only letters
        result_list.append(ch)

result = "".join(result_list)


#WEAK#



a,b = 20,30

for num in range(a, b + 1):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    if total == num:
        print(num, end=" ")




s = "Python is fun!"
print("Number of words:", len(s.split()))
print("Number of characters:", len(s))
print("Capitalized:", s.capitalize())





def Increment(lst):
    return [x + 100 for x in lst]


def perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


print("Perfect numbers between", a, "and", b, ":")
for num in range(a, b + 1):
    if perfect(num):
        print(num, end=" ")



import copy

students = {
    "Alice": [85, 90],
    "Bob": [70, 80]
}

shallow = copy.copy(students)
deep = copy.deepcopy(students)

shallow["Alice"][0] = 100   # modifies both
deep["Bob"][0] = 60         # only deep copy changed

print(shallow)
print(deep)

def cube_series(n):
    result = 0
    for i in range(1,n+1):
        term = i*i*i
        result += term

    return result

print(cube_series(3))




def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]




def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1




def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)




