# Genetic algorithm edited to fulfill the problem
# of placing vending machines in university facilities.

import numpy as np
import random
from utils import reproduce, mutate, put_major_value_coordinate

def gen_algorithm(population):
    """
    Genetic algorithm to find the solution to the problem by mutating and reproducing solutions.
    population: Population of solutions.
    """
    list_machines = []
    for i in range(len(population)):
        new_population = []
         
        for j in range(3):
            if put_major_value_coordinate(population) is None:
                return new_population
            # Choose a random coordinate from population for parent1
            parent1, parent2 = put_major_value_coordinate(population)
            child = reproduce(population)
            child = mutate(parent1, parent2, population, child)
            list_machines.append((parent1, parent2))
        return population, list_machines
    
