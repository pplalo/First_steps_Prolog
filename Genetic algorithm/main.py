# Matrix of probabilities assigning one  space into a map in order to determine
# the best position to place a vending machine in university facilities.

import numpy as np
import pprint
from genetic import gen_algorithm
from utils import replace_ones_with_M

matrix = np.zeros((17, 17))

array0 = np.zeros(17)
array1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0]
array2 = [0, 100, 40, 90, 90, 70, 80, 90, 80, 90, 80, 80, 50, 80, 0, 0, 0]
array3 = [0, 40, 40, 90, 20, 60, 0, 0, 0, 0, 0, 0, 60, 80, 80, 0, 0]
array4 = [0, 40, 50, 90, 20, 50, 0, 0, 0, 0, 0, 60, 50, 40, 0, 0, 0]
array5 = [0, 60, 30, 60, 20, 40, 20, 20, 20, 20, 20, 40, 40, 40, 20, 60, 0]
array6 = [0, 30, 20, 30, 20, 30, 40, 40, 40, 40, 40, 30, 20, 20, 20, 40, 1]
array7 = [0, 85, 80, 60, 20, 20, 40, 40, 40, 40, 40, 40, 0, 0, 80, 0, 0]
array8 = [0, 100, 0, 0, 20, 20, 50, 40, 50, 60, 70, 80, 80, 80, 80, 0, 0]
array9 = [0, 0, 0, 0, 10, 0, 0, 60, 20, 20, 20, 0, 0, 70, 70, 0, 0]
array10 = [0, 0, 0, 0, 10, 20, 0, 20, 50, 0, 0, 70, 1, 0, 0, 40, 0]
array11 = [0, 80, 0, 0, 0, 0, 0, 20, 80, 0, 0, 60, 1, 0, 0, 40, 80]
array12 = [0, 0, 0, 0, 0, 10, 80, 80, 80, 70, 60, 60, 50, 0, 0, 0, 0]
array13 = [0, 50, 50, 50, 40, 30, 0, 0, 0, 0, 20, 20, 20, 20, 20, 20, 20]
array14 = [0, 0, 50, 20, 0, 20, 0, 20, 0, 20, 20, 50, 0, 20, 20, 0, 0]
array15 = [0, 0, 0, 0, 0, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
array16 = np.zeros(17)

matrix = np.array([array0, array1, array2, array3, array4, array5, array6, array7, array8, array9, array10, array11, array12, array13, array14, array15, array16])
matrix2 = matrix
# matrix = np.ones((8,8))

i,j = gen_algorithm(matrix)
while len(i) == 0:
    i,j = gen_algorithm(matrix)

np.set_printoptions(linewidth=150, threshold=np.inf)
result = i
list_machines = j
print(result)
print(list_machines)

