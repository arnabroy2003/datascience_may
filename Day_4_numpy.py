# importing numpy
import numpy as np

# creating Arrays
# a = [1,2,3]

# b = [[1,2,3],
#      [4,5,6]]

# arr = np.array(a)
# arr2 = np.array(b)

# print(type(arr))
# print(arr2)

# Array Attributes

# b = [[1,2,3],
#     [4,5,6]]

# arr = np.array(b)

# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)

# print(arr)

# Useful Array Creation Functions

# Array of zeros
# zero_arr = np.zeros((3,2))
# print(zero_arr)

#Array of Ones
# one_arr = np.ones((4,4))
# print(one_arr)


# Identity Matrix
# indenty = np.eye(4)
# print(indenty)

#Range of numbers
# arr = np.arange(1,11)
# new_arr = arr.reshape(2,5)
# print(new_arr)

# arr = np.arange(1,100)
# new_arr = arr.reshape(3,33)
# print(new_arr)

#Jump
# arr = np.arange(1,10,2)
# print(arr)

#Evenly Spaced numbers
# esm = np.linspace(1,100,4)
# print(esm)

# esm = np.linspace(0,1,5)
# print(esm)

# Numpy Operations
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a+b)
# print(a*b)
# print(a/b)

# Aggregate Functions
arr = np.array(
    [[1,2,3], #6
     [4,5,6]] #15
)

first = np.max(arr[0])
print(first)
# # print(arr.sum())
# # print(arr.mean())
# # print(arr.max())
# # print(arr.min())
# # print(arr.std())

# print(arr.sum(axis=1)) # Row-wise sum
# print(arr.sum(axis=0)) # Column-wise sum

# print(arr.max(axis=1))
# print(arr.min(axis=0))

# Boolean Indexing
# arr = np.array([1,2,3,4,5])
# print(arr[arr>3])


# 1. create a 4x4 matrix and find means of each row
# 2. create a 3x3 matrix of random integer between 1 to 20 and perform
# row wise sum
# column wise max
# replace all element grater than 10 with 0