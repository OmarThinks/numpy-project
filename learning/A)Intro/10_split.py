import numpy as np 


array_1 = np.array([1,2,3,4,5,6,7,8,9])

new_array = np.array_split(array_1,3)
print(new_array) # [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]

new_array = np.array_split(array_1,2)# Not devideable over 2
print(new_array) # [array([1, 2, 3, 4, 5]), array([6, 7, 8, 9])]






array_2 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]]) # Contains 5 arrays

new_array = np.array_split(array_2,2)
print(new_array)
"""
[
	array([[1, 2],
       [3, 4],
       [5, 6]]), 
    array([[ 7,  8],
       [ 9, 10]])]
"""
