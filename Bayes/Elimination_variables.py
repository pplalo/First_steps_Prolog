import numpy as np

def eliminationAsk(X, e, bn):
    """
    Bayesian network inference using variable elimination.
    :param X: The query variable
    :param e: Observed values for variables E
    :param bn: A Bayesian network P(X1,...,Xn)
    :return: A distribution over X
    """
    factors = []
    
    for var in order(bn['VARS']):
        factors.append(make_factor(var, e, bn))
        
        # If var is a hidden variable, sum it out
        if var not in e and var != X:
            factors = sum_out(var, factors)
    
    return normalize(pointwise_product(factors))

def order(vars):
    """
    Orders the variables based on some heuristic.
    """
    return vars

def make_factor(var, e, bn):
    """
    Creates a factor for the given variable.
    """
    return 

def sum_out(var, factors):
    """
    Sums out the given variable from the list of factors.
    """
    return factors


def pointwise_product(factors):
    """
    Computes the pointwise product of the list of factors.
    """
    return factors


