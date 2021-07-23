import numpy as np


print("a_0")
a_0 = np.array(50)
print("a_0: " + str(a_0))
print("type(a_0): " + str(type(a_0)))
print("ndim(a_0): " + str(a_0.ndim))
"""
a_0
a_0: 50
type(a_0): <class 'numpy.ndarray'>
ndim(a_0): 0
"""



print("")
print("___")
print("a_1")
a_1 = np.array([1,2,3])
print("a_1: " + str(a_1))
print("type(a_1): " + str(type(a_1)))
print("ndim(a_1): " + str(a_1.ndim))
"""
a_1
a_1: [1 2 3]
type(a_1): <class 'numpy.ndarray'>
ndim(a_1): 1
"""








print("")
print("___")
print("a_2")
a_2 = np.array([[1,2,3],[4,5,6]])
print("a_2: " + str(a_2))
print("type(a_2): " + str(type(a_2)))
print("ndim(a_2): " + str(a_2.ndim))
"""
a_2
a_2: [[1 2 3]
 [4 5 6]]
type(a_2): <class 'numpy.ndarray'>
ndim(a_2): 2
"""



print("")
print("___")
print("a_3")
a_3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("a_3: " + str(a_3))
print("type(a_3): " + str(type(a_3)))
print("ndim(a_3): " + str(a_3.ndim))

"""
a_3
a_3: [[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
type(a_3): <class 'numpy.ndarray'>
ndim(a_3): 3
"""





print("")
print("___")
print("a_n")
a_n = np.array(40, ndmin=5)
print("a_n: " + str(a_n))
print("type(a_n): " + str(type(a_n)))
print("ndim(a_n): " + str(a_n.ndim))

"""
a_n
a_n: [[[[[40]]]]]
type(a_n): <class 'numpy.ndarray'>
ndim(a_n): 5
"""