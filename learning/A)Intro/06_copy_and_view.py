import numpy as np


array = np.array([1.1, 2.2, 3.3], dtype = float)

array_copy = array.copy()
array_view = array.view()





print("array_copy")
print(array_copy)
print(array_copy.dtype)
print(array_copy.base)
"""
array_copy
[1.1 2.2 3.3]
float64
None
"""


print("")
print("_____")
print("array_view")
print(array_view)
print(array_view.dtype)
print(array_view.base)

"""
array_view
[1.1 2.2 3.3]
float64
[1.1 2.2 3.3]
"""

print("")
print("_____")
print("array (Original)")
print(array)
print(array.dtype)
print(array.base)

"""
array (Original)
[1.1 2.2 3.3]
float64
None
"""










print("")
print("_____")
print("Changing Original")
array[0]= 100.3

print("Original: " + str(array))
print("Copy: " + str(array_copy))
print("View: " + str(array_view))



"""
Changing Original
Original: [100.3   2.2   3.3]
Copy: [1.1 2.2 3.3]
View: [100.3   2.2   3.3]
"""





print("")
print("_____")
print("Changing Copy")
array_copy[0]= 400.1



print("Original: " + str(array))
print("Copy: " + str(array_copy))
print("View: " + str(array_view))

"""
Changing Copy
Original: [100.3   2.2   3.3]
Copy: [400.1   2.2   3.3]
View: [100.3   2.2   3.3]
"""




print("")
print("_____")
print("Changing View")
array_view[0]= 1000.2

print("Original: " + str(array))
print("Copy: " + str(array_copy))
print("View: " + str(array_view))



"""
Changing View
Original: [1000.2    2.2    3.3]
Copy: [400.1   2.2   3.3]
View: [1000.2    2.2    3.3]
"""




