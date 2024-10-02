% test_first_steps.pl

:- begin_tests(dpll).

% Load the original file
:- [first_steps].

% Test cases for dpll_satisfiable/1
test(satisfiable) :-
    dpll_satisfiable("p v q").

test(unsatisfiable) :-
    \+ dpll_satisfiable("p ^ -p").

test(complex_satisfiable) :-
    dpll_satisfiable("p v q ^ -r -> s <-> t").

test(complex_unsatisfiable) :-
    \+ dpll_satisfiable("p ^ q ^ -p").

:- end_tests(dpll).

% Run the tests
:- run_tests.