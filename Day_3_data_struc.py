# List
# A list is an ordered collection of elements, enclosed with []

fruits = ["apple","banana","cherry"]

# print(fruits[0]) #apple

# # Negative Indexing
# print(fruits[-1]) #cherry

# # Changing Values
# fruits[0] = "pineapple"
# print(fruits)

# adding Elements
fruits.append("mango")
# print(fruits)

#inserting Elements
fruits.insert(2,"orange")
# print(fruits)

# remove Specific elements
# fruits.remove("apple")
# print(fruits)

# remove last element 
# fruits.pop()
# print(fruits)

# list length
# print(len(fruits)) #5

#Looping Through Lists

# for i in fruits:
#     print(i)

# List Slicing
# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0:4]) # [1, 2, 3, 4]
# print(numbers[1:4]) # [2, 3, 4]
# print(numbers[3:7]) # [4, 5, 6, 7]
# print(numbers[::2]) # [1, 3, 5, 7, 9]

# Tuple
# Tuple is like a list but Immutable (cannot be changed)

# colors = ("red","green","blue")
# # print(colors[1])

# Errors
# colors[0] = "Yellow"


# Dictionary
# "Key"     "Value"  
# "Water" = "Pani"
# "Water" = "Tanni"

# A dictionary is an unordered collectioon of key-value pairs, enclosed in {}

# Eng_Tam = {
#     "Water": "Tanni",
#     "Fire": "nerapu"
# }

# print(Eng_Tam["Fire"])


# student = {
#     "name": "Attadeep",
#     "age": 22,
#     "course": "Python"
# }

#Accessing Values
# print(student["age"])

#Adding Key-Value
# student["city"] = "Mumbai"
# print(student)

#changing value
# student["age"] = 70
# print(student)

#remove key
# student.pop("course")
# print(student)

# get all keys
# print(student.keys())

# # get all values
# print(student.values())

#Check key existance
# if "age" in student:
#     print("yes")
# else:
#     print("No")

# Nested Dictionaries

# students = {
#     "s1": {"name": "Attadeep", "age": 22},
#     "s2": {"name": "Sathipriya", "age": 32}
# }

# print(students["s1"]["age"]) #22


