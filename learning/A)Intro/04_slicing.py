import numpy as np



arr0 = np.array([0,1,2,3,4,5,6,7,8])

print(arr0[1:5]) # from index 1 to index 5
# [1 2 3 4]
print(arr0[1:5:2]) # from index 1 to index 5 with step 2
# [1 3]
print(arr0[:5]) # from start to index 5 with step 2
# [0 1 2 3 4]
print(arr0[::3]) # from start to end with step 3
# [0 3 6]

"""Negative Slicing"""

print(arr0[-2:]) # last 2 elements??????
# [7 8]




print("")
print("2D Slicing")


arr_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr_2[0:1,1:4])
# [[2 3 4]]
