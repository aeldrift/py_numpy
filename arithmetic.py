import numpy as np

var = np.array([1,2,3,4])
var_add = var+3
print("After adding 3 to each element:",var_add)

var_sub = var - 3
print("After subtracting 3 from each element:",var_sub)

var_mul = var * 3
print("After multiplying each element by 3:",var_mul)

var_div = var / 3
print("After dividing each element by 3:",var_div)

var_mod = var %3
print("After taking modulo 3 of each element:",var_mod)

var1 = np.array([10,20,30,40])
var_add1 = var + var1
print("After adding two arrays element-wise:",var_add1)

# OR
var_add1 = np.add(var, var1)
print("After adding two arrays element-wise using add():",var_add1)

var_add1= np.add(var,3)
print("After adding two arrays element-wise using add():",var_add1)

# FOr 2-D array:
