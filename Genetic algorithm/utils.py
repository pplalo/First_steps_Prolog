import numpy as np

def fitness(row, col, n, population):
    """
    Fitness function that evaluates the quality of a solution.
    """
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
    child[parent1][parent2] = 1
    child = fitness(parent1, parent2, len(child), child)
    population = child + population
    for i in range(len(population)):
        for j in range(len(population)):
            if population[i][j] == -2:
                population[i][j] = -1
            if population[i][j] == 2:
                population[i][j] = 1
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

def get_random_zero_coordinate(arr):
    """
    Returns separately the row and column coordinates of an array whose values are zero.
    arr: NumPy array.
    return: Two values, row and column.
    """
    # Get the coordinates of the elements that are zero
    zero_coords = np.argwhere(arr == 0)
    
    if zero_coords.size == 0:
        return None
    
    # Select a random coordinate from the found coordinates
    random_index = np.random.choice(len(zero_coords))
    row, col = zero_coords[random_index]
    return row, col
