import numpy as np

var1 = np.array([1,2,3,4])

var2 = np.array([1,2,3,5])

print("var1 + var2 is:\n", var1 + var2)

var3 = np.array([1,2])

var4 = np.array([[1],[3]])
print("var1 is:\n", var3)
print("var2 is:\n", var4)
print("var3 + var4 is:\n", var3 + var4)

a = np.array([1, 2, 3])      # (3,)
b = np.array([[1], [2]])    # (2,1)

print("result a+b is:\n", a + b)

# when shapes are not compatible, gives error 

''' c = np.array([[1,2],[3,4]])      
d = np.array([1,2,3])    

print("result c +d  is:\n", c + d)''' 

c = np.array([1, 2, 3])      # shape (3,)
d = np.array([[2], [1]])     # shape (2,1)

print("c > d is:\n",c > d)

print("c < d is:\n",c < d)

print("c == d is:\n",c == d)

a = np.array([0, 1, 2])          # shape (3,)
b = np.array([[10], [20]])       # shape (2,1)

print(np.sin(a + b))             
print(np.sin(a+b).shape)

arr = np.zeros((3,3))
arr[:, 2] = np.array([1,2,3])  # Broadcast along columns
print(arr)

# indexing 
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # 10
print(arr[-1])  # 50

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[0, 1])  # 2 → row 0, column 1
print(arr2d[2, 0])  # 7 → row 2, column 0



a = np.array([10,20,30,40])
print("indexing is")
print(a[2])
print(a[-1]) 
print(a[:])
print(a[1:3]) # [20 30]
print()
print(a[2:3]) # 30
# print(a[-1:5]) 

# print(a[::2])

# slicing: arr[start:stop:step]
arr = [10, 20, 30, 40, 50, 60]

print(arr[1:4])    # [20, 30, 40] → from index 1 to 3
print(arr[:3])     # [10, 20, 30] → from start to index 2
print(arr[3:])     # [40, 50, 60] → from index 3 to end
print("index",arr[::2])    # [10, 30, 50] → every 2nd element
print(arr[::-1])   # [60, 50, 40, 30, 20, 10] → reversed list
print(arr[::-2])  # [60, 40, 20]
print(arr[::-3]) # [60, 30]

