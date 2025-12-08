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