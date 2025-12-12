import numpy as np 
myarr=np.array([1,2,3,4,5],np.int8) #np.int8 : numpy types reference
print(myarr)
print(myarr[0])
print(myarr.dtype)
print(myarr.size)

myarr2=np.array([[1,2,3,4,5],[12,13,14,0,16]],np.int8) # 2-D array
print('myarr2 is:',myarr2)
print(myarr2[0,1]) # accessing 2-D array element
myarr2[0,1]=9 # modifying 2-D array element
print(myarr2) #updated array value

import timeit

size = 1000000
list_time = timeit.timeit('[j**4 for j in range(1,9)]', number=10)
print(f"Python list comprehension: {list_time:.6f} seconds")    

numpy_time = timeit.timeit('np.arange(1,9)**4', globals=globals(), number=10)
print(f"NumPy vectorized: {numpy_time:.6f} seconds")

l=[]
for i in range(1,5):
    int_1=int(input("enter value:", ))
    l.append(int_1)
print(np.array(l))
print("dimension of myarr is:",myarr.ndim)
print("dimension of myarr2 is:",myarr2.ndim)

#creating a N-Dimensional array
n_arr=np.array([10,11,12,1,14],ndmin=5)
print(n_arr)
print("dimension of n_arr is:",n_arr.ndim)

# creatinga zero array:
arr_zero = np.zeros(4)
print("Zero array:",arr_zero)

arr_zero1 = np.zeros((3,4)) #2-D array
print("Zero1 array:\n",arr_zero1)

# creating a one array:
arr_one=np.ones (4)
print("Ones array:",arr_one)

# creating ann empty array:
arr_empty=np.empty(4)
print("Empty array:",arr_empty)

# creating a range array:
arr_range=np.arange(10)
print("Range array:",arr_range)
arr_range1=np.arange(1,10,3) #start,stop,step
print("Range1 array:",arr_range1)

#creating a diagonal array:
arr_diag=np.eye(3)
print("Diagonal array:\n",arr_diag)

arr_diag1=np.eye(3,5)
print("Diagonal array1:\n",arr_diag1)

# creating a linspace array:
arr_linspace=np.linspace(0,20,num=5) #start,stop,num of elements
print("Linspace array:",arr_linspace)

# rand() function:  nos. btw 0 and 1
var=np.random.rand(4)
print("Random array:",var)

var=np.random.rand(2,5)
print("Random 2-D array:",var)

# randn() function:  nos. close to 0, +ve or -ve
var1 = np.random.randn(4)
print("Random array:",var1)

# ranf() function:  nos. btw 0 and 1 but 1 is excluded
var2 = np.random.ranf(4)
print("Random array:",var2)
var2 = np.random.ranf((2,3))
print("Random 2-D array:",var2)

# randint() function:  nos. btw a given range
var3 = np.random.randint(1,10,4) #min,max,total_values (or size)
print("Random array:",var3)

var3 = np.random.randint(1,10,(2,2)) 
print("Random 2-D array:",var3)

# seed() function: to generate same random nos. again and again
np.random.seed(10)  # seed “freezes” NumPy’s random generator to a known starting point.
var4 = np.random.rand(4)
print("Random array with seed 10:",var4)

# accessing array elements:
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a[1,5])
print(a[:, 3])