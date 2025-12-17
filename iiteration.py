
# iteration:
import numpy as np

x=[1,2,3,4,5]
print("printing using for loop:")
for i in x:
    print(i)

print("value of i with indexing:")
for i in x[1:4]:
    print(i)

arr = np.array([10,20,30,40,50])
print("arr is:",arr)

for i in arr:
    print(i)


arr2d = np.array([[100,200,300],[400,500,600]])
print("arr2d is:\n",arr2d)
print()
for j in arr2d:
    print(j)

# iteration in 2-D array:
print("iteration in 2-D array:")
for j in arr2d:
    for k in j:
        print(k)

arr = np.array([[1,2,3,4],[5,6,7,8]],ndmin=7)
print("dimensionof array arr is:",arr.ndim)

for i in np.nditer(arr):
    print(i)

for i in np.nditer(arr,flags=['buffered'],op_dtypes=["S"]):
    print(i)

for i in np.nditer(arr):
    print("i is:", i)

# astype():
new_arr = arr.astype("S")
print("new_arr is:\n",new_arr)

# readwrite():
# example:1
for i in np.nditer(arr,op_flags=['readwrite']):
      i[...] = i * 1
print("i is:",i)

# example:2
arr = np.array([1, 2, 3])

for i in np.nditer(arr, op_flags=['readwrite']):
    i[...] *= 10  # as 3 elements are there, so loop'll run 3 times

print(arr)

# Row- major order (C order):
arr = np.array([[1,2,3],[4,5,6]])
for i in np.nditer(arr, order='C'):
    arr[:] += 10
    print(i) # 11 12 13 14 15 16

print()
# or
arr = np.array([[1,2,3],[4,5,6]])
for i in np.nditer(arr, op_flags=['readwrite']):
    arr[:] += 10
    print(i) #11 22 33 44 55 66

print()

arr = np.array([[1,2,3],[4,5,6]])
for i in np.nditer(arr, op_flags=['readwrite']):
    i[...] += 10
    print(i)

''' or use( returns 1-D copy of an array):
  for every_element in arr.flatten():
         modify(element)'''

# Fortran order (F order):
for i in np.nditer(arr, order='F'):
    arr[:] += 10
    print(i)

''' 
# arr.flatten(order='C'/'F') → flatten array in memory order

# np.copy(arr, order='C'/'F') → copy array with specified memory layout

# reshape(-1, order='C'/'F') → reshape using C or F order '''

