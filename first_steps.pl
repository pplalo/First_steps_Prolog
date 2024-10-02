% Obtener la clausulas y simbolos a partir de un enunciado con lógica proposicional
dpll_satisfiable(Proposition) :-
    get_clauses(Proposition, Clauses),
    get_symbols(Proposition, Symbols),
    dpll(Clauses, Symbols, []).


is_empty([]).

% Predicado que verifica si una cláusula es falsa en el modelo
clause_false_in_model(Clause, Model) :-
    \+ (member(Literal, Clause), member(Literal, Model)).

% Predicado que encuentra un símbolo puro y su valor
find_pure_symbol([], _, _, _) :- fail.
find_pure_symbol([Symbol|Symbols], Clauses, Model, (Symbol, true)) :-
    is_pure_symbol(Symbol, Clauses, Model, true), !.
find_pure_symbol([Symbol|Symbols], Clauses, Model, (Symbol, false)) :-
    is_pure_symbol(Symbol, Clauses, Model, false), !.
find_pure_symbol([_|Symbols], Clauses, Model, PureSymbol) :-
    find_pure_symbol(Symbols, Clauses, Model, PureSymbol).

% Predicado que verifica si un símbolo es puro
is_pure_symbol(Symbol, Clauses, Model, true) :-
    \+ (member(Clause, Clauses), member(-Symbol, Clause)).
is_pure_symbol(Symbol, Clauses, Model, false) :-
    \+ (member(Clause, Clauses), member(Symbol, Clause)).

% Predicado que encuentra una cláusula unitaria y su valor
find_unit_clause([], _, none).
find_unit_clause([Clause|Clauses], Model, (P, Value)) :-
    unit_clause(Clause, Model, (P, Value)), !.
find_unit_clause([_|Clauses], Model, UnitClause) :-
    find_unit_clause(Clauses, Model, UnitClause).

% Predicado que verifica si una cláusula es unitaria y su valor
unit_clause([Literal], Model, (P, Value)) :-
    \+ member(Literal, Model),
    (Literal > 0 -> P = Literal, Value = true ; P is -Literal, Value = false).


% Define la función generada con tres parámetros
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

% Obtener las clausulas a partir de un enunciado con lógica proposicional con el operador "v, ^, ->, <->"
get_clauses(Proposition, Clauses) :-
    split_string(Proposition, ",", "", Clauses).

% Obtener los simbolos a partir de un enunciado con lógica proposicional
get_symbols(Proposition, Symbols) :-
    split_string(Proposition, ",", "", SymbolList),
    list_to_set(SymbolList, Symbols).

% Ejemplo de uso
?- dpll_satisfiable("1,2,-3,4,-5"). % true
?- dpll_satisfiable("1,2,-3,4,-5,6"). % false




