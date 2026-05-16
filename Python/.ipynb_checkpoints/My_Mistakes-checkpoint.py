
'''Code 1 Start'''


# print("Hello World")
# n = int(input("Enter the number of elements in list"))
# list = []

# for i in range(n):
#     print(f"Enter element {i}")
#     list[i] = input()
#     list.append()
# print(list)



n = int(input("Enter the number of elements in list\n"))
list = []

for i in range(n):
    print(f"Enter element {i}")
    value = input()
    list.append(value)

print(list)


n = int(input("Enter the number of elements in list\n"))
list = []

for i in range(n):
    value = input(f"Enter the element {i+1} \n")
    list.append(value)

print(list)


'''Code 1 End'''