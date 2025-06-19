# age = 8

# if age>=18:
#     print("You can Vote!")
# elif age<=10:
#     print("You are a baby")
# else:
#     print("You can't vote!")

# b = int(input("Enter a number: "))

# print("You Write: ",b)

# b=input("enter your name:")
# print("Hello",b)

# n = int(input("Enter a number: "))

# if (n%2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

# name = "John"

# for i in name:
#     print(i)

# for i in range(1,6,2):
#     print(i)

# i = 1

# while (i<=5):
#     print("Tarun")
#     print(i)
#     i = i + 1

# name = input("Enter your name: ")
# n = int(input("Enter time: "))

# for i in range(1,n+1):
#     print(name)
n = int(input("Enter the range: "))

for i in range(1,n+1):
    for j in range(1,i+1): 
        print(j,end=" ") 
    print()      

