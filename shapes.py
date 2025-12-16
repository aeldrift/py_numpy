import numpy as np

''' 1-D array → shape gives number of elements.
2-D array → shape gives (rows, columns).
3-D or higher → shape gives (depth, rows, columns) or more axes. '''

# to get shape of an array
arr = np.array([[1,2,3],[4,5,6]])
print("Number of dimensions is:", arr.ndim)
print("Shape of array is:", arr.shape)

# 1-D array
a = np.array([10, 20, 30, 40, 50])
print("1-D array shape is:", a.shape) #(5,)

# 2-D array
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("2-D array shape is:", b.shape) #(2, 3)

# 3-D array
c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
print("3-D array shape is:", c.shape) #(3, 2, 2)

# 4-D array
d = np.zeros((3, 2, 3, 2))
print(d)
print("4-D array shape is:", d.shape) #(5, 2, 3, 4)

d = np.array([1,2,3,4],ndmin=4)
print("the array d is", d)
print("dimension of d is:",d.ndim)
print("4-D array shape is:", d.shape) #(1,1,1,4)

one = d.reshape(-1)
print("reshaped array is:", one)
print("reshaped array shape is:", one.shape) #(4,)
