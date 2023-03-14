"""
This file is just for me to test random things.
"""
import numpy as np

array1 = np.array([1, 2, 3, 4,5,6,7,8])
# splitting the array into three
new_array1 = np.array_split(array1, 4)
print(new_array1[0])
print(array1)
