import numpy as np 


print("")
print("array0")
print("____")
array0 = np.array(5)
print(array0.shape) # ()
print(array0.ndim) # 0	

print("")
print("array1")
print("____")
array1 = np.array([1,2,3,4])
print(array1.shape) # (4, )
print(array1.ndim) # 1	


print("")
print("array2")
print("____")
array2 = np.array([[1,2,3,4],[5, 6, 7, 8]])
print(array2.shape) # (2,4)
print(array2.ndim) # 2

print(array2[1,3]) # 8



print("")
print("array5")
print("____")
array5 = np.array([5, 6, 7, 8], ndmin = 5)
print(array5) # [[[[[5 6 7 8]]]]]
print(array5.shape) # (1,1,1,1,4)
print(array5.ndim) # 5
print(array5[0,0,0,0,2]) # 7







