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