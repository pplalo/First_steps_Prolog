def dpll(clauses, symbols, model):
    """
    DPLL algorithm to determine the satisfiability of a propositional logic formula.
    
    :param clauses: List of clauses (each clause is a list of literals)
    :param symbols: List of propositional symbols
    :param model: Current model (dictionary of symbol assignments)
    :return: True if the formula is satisfiable, False otherwise
    """
    # Base case: if all clauses are true in the model, return True
    if all(is_clause_true(clause, model) for clause in clauses):
        return True
    
    # Base case: if any clause is false in the model, return False
    if any(is_clause_false(clause, model) for clause in clauses):
        return False
    
    # Find a pure symbol and its value
    pure_symbol, value = find_pure_symbol(symbols, clauses, model)
    if pure_symbol is not None:
        new_model = model.copy()
        new_model[pure_symbol] = value
        new_symbols = [s for s in symbols if s != pure_symbol] ## remove the pure symbol from the list of symbols
        return dpll(clauses, new_symbols, new_model)
    
    # Find a unit clause and its value
    unit_clause, value = find_unit_clause(clauses, model)
    if unit_clause is not None:
        new_model = model.copy()
        new_model[unit_clause] = value
        new_symbols = [s for s in symbols if s != unit_clause]
        return dpll(clauses, new_symbols, new_model)
    
    # Choose the first symbol from the list of symbols
    P = symbols[0]
    rest = symbols[1:]
    
    # Try assigning True to the symbol
    new_model_true = model.copy()
    new_model_true[P] = True
    if dpll(clauses, rest, new_model_true):
        return True
    
    # If assigning True fails, try assigning False
    new_model_false = model.copy()
    new_model_false[P] = False
    return dpll(clauses, rest, new_model_false)

def is_clause_true(clause, model):
    """
    Check if a clause is true in the given model.
    
    :param clause: List of literals
    :param model: Current model (dictionary of symbol assignments)
    :return: True if the clause is true in the model, False otherwise
    """
    return any(literal in model and model[literal] for literal in clause)

def is_clause_false(clause, model):
    """
    Check if a clause is false in the given model.
    
    :param clause: List of literals
    :param model: Current model (dictionary of symbol assignments)
    :return: True if the clause is false in the model, False otherwise
    """
    return all(literal in model and not model[literal] for literal in clause)

def find_pure_symbol(symbols, clauses, model):
    """
    Find a pure symbol and its value.
    
    :param symbols: List of propositional symbols
    :param clauses: List of clauses
    :param model: Current model (dictionary of symbol assignments)
    :return: Tuple (pure_symbol, value) if a pure symbol is found, (None, None) otherwise
    """
    for symbol in symbols:
        is_pure = True
        # Value represents the boolean value of the symbol in the model
        value = None
        # Check if the symbol has the same value in all clauses
        for clause in clauses:
            if symbol in clause:
                if value is None:
                    value = True
                elif value is False:
                    is_pure = False
                    break
            elif f"-{symbol}" in clause:
                if value is None:
                    value = False
                elif value is True:
                    is_pure = False
                    break
        if is_pure and value is not None:
            return symbol, value
    return None, None

def find_unit_clause(clauses, model):
    """
    Find a unit clause and its value.
    
    :param clauses: List of clauses
    :param model: Current model (dictionary of symbol assignments)
    :return: Tuple (unit_clause, value) if a unit clause is found, (None, None) otherwise
    """
    for clause in clauses:
        unassigned_symbols = [symbol for symbol in clause if symbol not in model and f"-{symbol}" not in model]
        if len(unassigned_symbols) == 1:
            unit_symbol = unassigned_symbols[0]
            value = True if unit_symbol[0] != '-' else False
            return unit_symbol.lstrip('-'), value
    return None, None

# Example usage
clauses = [[1, 2, -3], [-1, -2, 3], [1,-2, 3]]
symbols = [1, 2, 3]
model = {}
print(dpll(clauses, symbols, model))  # Output: True or False depending on satisfiability