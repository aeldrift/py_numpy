import numpy as np

var = np.array([1,2,3,4])
var_add = var + 3
print("After adding 3 to each element:",var_add)

var_sub = var - 3 # np.subtract(var,3)
print("After subtracting 3 from each element:",var_sub)

var_mul = var * 3 # np.multiply(var,3)
print("After multiplying each element by 3:",var_mul)

var_div = var / 3 # np.divide(var,3)
print("After dividing each element by 3:",var_div)

var_mod = var %3 # np.mod(var,3)
print("After taking modulo 3 of each element:",var_mod)

var_power = var ** 3 # np.power(var,3)
print("After raising each element to the power of 3:",var_power)

v=np.array([1,2], dtype=float)
print("recip is:", np.reciprocal(v))

var_recip = 1/var # np.reciprocal(var)
print("After taking reciprocal of each element:",var_recip)


var1 = np.array([10,20,30,40])
var_add1 = var + var1
print("After adding two arrays element-wise:",var_add1)


# OR
var_add1 = np.add(var, var1)
print("After adding two arrays element-wise using add():",var_add1)

var_add1= np.add(var,3)
print("After adding two arrays element-wise using add():",var_add1)

# For 2-D array:
arr = np.array([[1,2,3],[4,5,6]])
arr1 = np.array([[7,8,9],[10,11,12]])
arr_add = arr + arr1
print("arr is:\n",arr,"\n arr1 is:\n",arr1)
print("After adding two 2-D arrays element-wise:\n",arr_add)

arr_sub = arr + arr1
print("After subtracting two 2-D arrays element-wise:\n",arr_sub)

arr_mul = arr * arr1
print("After multiplying two 2-D arrays element-wise:\n",arr_mul)

arr_div = arr / arr1
print("After dividing two 2-D arrays element-wise:\n",arr_div)

arr_mod = arr % arr1
print("After taking modulo of two 2-D arrays element-wise:\n",arr_mod)

# Arithmetic Functions:
a = np.array([1,2,3,4,0,7,5])

print("Original array:",a)
print("min value is:", np.min(a),"argmin is:", np.argmin(a))

print("max valule is:", np.max(a),"argmax is:", np.argmax(a))

print("sum is:", np.sum(a))

print("mean is:", np.mean(a))

a1 = np.array([[9,9,3],[2,4,6]])
print("min is:",np.min(a1, axis=1)) # row-wise min

print("min is:",np.min(a1, axis=0)) # column-wise min

print("sqrt is:",np.sqrt(a1))

# to find square root of each element of an array
a = np.array([1,2,0])
print("sqrt of a  is:\n",np.sqrt(a))

print("sqrt of a1 is:\n",np.sqrt(a1))

# to find trignometric values of each element of an array 

print("sin of a is:",np.sin(a)) # sin funcn
print("cos of a1 is:\n",np.cos(a1)) # cos funcn
print("tan of a is:",np.tan(a)) # tan funcn

''' # for funcns like: 
cosec funcn =1/np.sin(a1)
 # sec funcn =1/np.cos(a1)
 # cot funcn= 1/np.tan(a1) '''

# cumsum: cumulative sum of elements
array = np.array([1,2,3,4])
print("cumsum of array is:",np.cumsum(array))