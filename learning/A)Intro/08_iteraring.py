import numpy as np 



print("")
print("1D")
print("_____")
array1 = np.array([1,2,3,4])
for x in array1:
	print(x)

"""
1
2
3
4
"""







print("")
print("2D")
print("_____")
array2 = np.array([[1,2,3,4],[5,6,7,8]])
for x in array2:
	print(x)

"""
[1 2 3 4]
[5 6 7 8]
"""

for x1 in array2:
	for x2 in x1:
		print(x2)

"""
1
2
...
8
"""



print("nditer")
for x in np.nditer(array2):
	print(x)
"""
1
2
...
8
"""

print("ndenumerate")
for index, value in np.ndenumerate(array2):
	print(index,value)

"""
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
"""
