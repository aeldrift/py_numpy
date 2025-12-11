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

y=np.array([1,2,3,4],dtype = "f")
print(y.dtype)