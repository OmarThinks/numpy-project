import numpy as np 


array = np.array([1,2,3,4])
print(array.dtype)
# int32


array = np.array(["Hi"])
print(array.dtype)
# <U2


array = np.array([1.1, 2.2, 3.3])
print(array.dtype)
# float64




# Creating an array while defining the data type
array = np.array([1,2,3,4], dtype = "S")
print(array.dtype)
# |S1

print(array)
# [b'1' b'2' b'3' b'4']
# Recorded as string



try:
	array = np.array(["Hi"], dtype="i")
except Exception as e:
	print("Can not Convert this string to integer")


print("_____")
print("Converting array types")


array = np.array([1.1,1.2])
array2 = array.astype("i")


print(array.dtype) # float64
print(array2.dtype) # int32

print(array) # [1.1 1.2]
print(array2) # [1 1]



print("_____")
print("Converting array types 2")

array = np.array([1.1,1.2])
array2 = array.astype(int)


print(array.dtype) # float64
print(array2.dtype) # bool

print(array) # [1.1 1.2]
print(array2) # [True True]



print("_____")
print("Converting array types 3")

array = np.array([1.1,1.2])
array2 = array.astype(bool)


print(array.dtype) # float64
print(array2.dtype) # float64

print(array) # [1.1 1.2]
print(array2) # [1 1]





print("______")
print("Creating an array with a python data type")




array = np.array([1.1,2.2,3.3], dtype=int)
print(array.dtype) # int32
print(array) # [1 2 3]
