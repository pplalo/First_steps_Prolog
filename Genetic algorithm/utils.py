import numpy as np

# Auxiliary functions to change certain conditions of the board 
# at the moment when a queen is placed in a position
def change_values_around_coordinate(row, col, n, assignment):
    """
    Function that changes 5 values up, down, left and right starting from coordinate row col de
    """
    value = 0
    value = assignment[row][col]
    for i in range(max(0, row-5), row):
        assignment[i][col] = 0
        for j in range(n):
            if i+j == row+col or i-j == row-col:
                assignment[i][j] = 0

    for i in range(max(0, col-5), col):
        assignment[row][i] = 0

    for i in range(col,min(col+5,n)):
        assignment[row][i] =  0

    for i in range(row,min(row+5,n)):
        assignment[i][col] = 0 
        for j in range(n):
            if i+j == row+col or i-j == row-col:
                assignment[i][j] = 0

    assignment[row][col] = value
            
    return assignment

def fitness(row, col, n, population):
    """
    Fitness function that evaluates the quality of a solution.
    row: int
    col: int
    n: int
    population: Numpy array
    """
    change_values_around_coordinate(row,col,n,population)

    return population

def reproduce(population):
    """
    Function that crosses two parents to produce a child.
    """
    child = population
    return child

def mutate(parent1, parent2, population, child):
    """
    Function that mutates a child.
    """
    child[parent1][parent2] = -1
    child = fitness(parent1, parent2, len(child), child)
    population = child
    return population

def is_valid_child(child, parent1, parent2):
    """
    Function that returns True if the child is valid.
    """
    value = child[parent1][parent2]
    if isinstance(value, np.ndarray):
        if np.any(value != 0):
            return False
    else:
        if value != 0:
            return False
    return True

def put_major_value_coordinate(arr):
    '''
    Returns separately the row and column coordinates of an array whose values are the highest.
    '''
    # Get the coordinate of the elements that are the highest
    max_coords = np.argwhere(arr == np.max(arr))

    if max_coords.size == 0:
        return None
    
    # Select the coordinate of the highest value from the found coordinates
    row, col = max_coords[0]
    return row,col

def replace_ones_with_M(arr):
    """
    Reemplaza todos los valores de -1 con 'M' en un arreglo de NumPy.
    arr: Arreglo
    return: Arreglo modificado con 'M' en lugar de -1.
    """
    arr = arr.astype(object)  # Convertir el arreglo a tipo object para permitir strings
    arr[arr == -1] = 'M'
     
    return arr