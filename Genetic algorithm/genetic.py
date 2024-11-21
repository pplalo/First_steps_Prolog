import numpy as np
import random
from utils import fitness, reproduce, mutate, is_valid_child, get_random_zero_coordinate

def gen_algorithm(population):
    """
    Genetic algorithm to find the solution to the problem by mutating and reproducing solutions.
    population: Population of solutions.
    """
    for i in range(len(population)):
        new_population = []
         
        for j in range(len(population)):
            if get_random_zero_coordinate(population) is None:
                return new_population
            # Choose a random coordinate from population for parent1
            parent1, parent2 = get_random_zero_coordinate(population)
            child = reproduce(population)
            if is_valid_child(child, parent1, parent2):
                child = mutate(parent1, parent2, population, child)
        return population