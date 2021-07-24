import numpy as np 


array1 = [[1,2],[3,4]]
array2 = [[5,6],[7,8]]

print("Concatenate")
print("_________")

array3_0 = np.concatenate((array1,array2), axis=0)
print(array3_0)
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""


array3_1 = np.concatenate((array1,array2), axis=1)
print(array3_1)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""





print("")
print("Stack")
print("_________")


array1 = [1,2, 3,4]
array2 = [5,6,7,8]




array3_0 = np.stack((array1,array2), axis=0)
print(array3_0)
"""
[[1 2 3 4]
 [5 6 7 8]]
"""

array3_1 = np.stack((array1,array2), axis=1)
print(array3_1)
"""
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
"""


















