% Obtains the clauses and symbols from a propositional logic statement
dpll_satisfiable(Proposition) :-
    get_clauses(Proposition, Clauses),
    get_symbols(Proposition, Symbols),
    dpll(Clauses, Symbols, []).

is_empty([]).

% Predicate that checks if a clause is false in the model
clause_false_in_model(Clause, Model) :-
    \+ (member(Literal, Clause), member(Literal, Model)).

% Predicate that finds a pure symbol and its value
find_pure_symbol([], _, _, _) :- fail.
find_pure_symbol([Symbol|Symbols], Clauses, Model, (Symbol, true)) :-
    is_pure_symbol(Symbol, Clauses, Model, true), !.
find_pure_symbol([Symbol|Symbols], Clauses, Model, (Symbol, false)) :-
    is_pure_symbol(Symbol, Clauses, Model, false), !.
find_pure_symbol([_|Symbols], Clauses, Model, PureSymbol) :-
    find_pure_symbol(Symbols, Clauses, Model, PureSymbol).

% Predicate that checks if a symbol is pure
is_pure_symbol(Symbol, Clauses, Model, true) :-
    \+ (member(Clause, Clauses), member(-Symbol, Clause)).
is_pure_symbol(Symbol, Clauses, Model, false) :-
    \+ (member(Clause, Clauses), member(Symbol, Clause)).

% Predicate that finds a unit clause and its value
find_unit_clause([], _, none).
find_unit_clause([Clause|Clauses], Model, (P, Value)) :-
    unit_clause(Clause, Model, (P, Value)), !.
find_unit_clause([_|Clauses], Model, UnitClause) :-
    find_unit_clause(Clauses, Model, UnitClause).

% Predicate that checks if a clause is unit and its value
unit_clause([Literal], Model, (P, Value)) :-
    \+ member(Literal, Model),
    (Literal > 0 -> P = Literal, Value = true ; P is -Literal, Value = false).

% Define the generated function with three parameters
dpll(Clauses, Symbols, Model) :-
    is_empty(Clauses), !, true.

dpll(Clauses, Symbols, Model) :-
    member(Clause, Clauses),
    clause_false_in_model(Clause, Model), !, false.

dpll(Clauses, Symbols, Model) :-
    find_pure_symbol(Symbols, Clauses, Model, (P, Value)),
    P \= none, !,
    % Add the pure symbol to the model
    dpll(Clauses, Symbols, [P=Value|Model]).

dpll(Clauses, Symbols, Model) :-
    find_unit_clause(Clauses, Model, (P, Value)),
    P \= none, !,
    % Add the unit clause to the model
    dpll(Clauses, Symbols, [P=Value|Model]).

% p = first(symbols)
dpll(Clauses, Symbols, Model) :-
    member(P, Symbols), !,
    % Add the symbol to the model
    dpll(Clauses, Symbols, [P=true|Model]).

%rest = rest(symbols)
dpll(Clauses, Symbols, Model) :-
    member(P, Symbols), !,
    % Add the symbol to the model
    dpll(Clauses, Symbols, [P=false|Model]).

% Obtain the clauses from a propositional logic statement with the operator "v, ^, ->, <->"
get_clauses(Proposition, Clauses) :-
    split_string(Proposition, ",", "", Clauses).

% Obtain the symbols from a propositional logic statement
get_symbols(Proposition, Symbols) :-
    split_string(Proposition, ",", "", SymbolList),
    list_to_set(SymbolList, Symbols).

% Examples
?- dpll_satisfiable("1,2,-3,4,-5"). % true
?- dpll_satisfiable("1,2,-3,4,-5,6"). % false
