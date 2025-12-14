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