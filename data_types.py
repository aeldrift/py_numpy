import numpy as np
var = np.array([1,2,3,4])
print("Data Type: " ,var.dtype)

var1 = np.array([1.0,2,3,4])
print("Data Type: " ,var1.dtype)


var2 = np.array(["A","b","D","e"])
print("Data Type: " ,var2.dtype)

var3 = np.array(["A","b","D","e",3,4,9,6])
print("Data Type: " ,var3.dtype)

# To change dtype of an array:

x=np.array([1,2,3,4],)
print(x.dtype)

x1=np.array([1,2,3,4],dtype=np.int8)
print(x1.dtype)

x2=np.array([1,2,3,4],dtype = "f")
print(x2.dtype)

# converting as a functon
x3 = np.array([1,2,3,4]) # To convert directly

new= x3.astype(np.float64)
print(new.dtype)   
   
   # OR

x3=np.array([1,2,3,4])
new=np.float32(x3)
print("Data Type: ",x3.dtype)
print(x3)
print("new array is",new)
print(new.dtype)

# converting again 
new1=np.int_(new)
print(new1)
print("Data Type: ",new1.dtype)

# Arithmetic Operations on arrays using numpy
a = np.array([2,3,4,5])
b = np.array([1,2,3,4])
c = a+b
c1 = a-b
c2 = a*b
c3 = a/b
print(c)
print(c1)
print(c2)
print(c3)

# on performing arithmetic operations on lists
a=[1,2,3,4]
b=[5,6,7,8]
c=a+b   # will concatenate the lists
print("concatenate gives",c)

# to add two lists element wise 
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])

print("addition gives", c)

# Using zip() and list comprehension
c = [x + y for x, y in zip(a, b)]
print("Using zip addition gives c as:", c)