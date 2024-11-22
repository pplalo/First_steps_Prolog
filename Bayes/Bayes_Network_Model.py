# The following code was inspired and obtained from the following link:
# https://www.kaggle.com/code/scratchpad/notebookbdb90e061e/edit
# Library Used: Pomegranate
# Library author: Jacob Schreiber(jmschreiber91@gmail.com) 

from pomegranate import *

# The guests initial door selection is completely random
a = DiscreteDistribution({'1': 1./10, '0': 9./10})

b = ConditionalProbabilityTable(
        [[ '0', '0', 0.1 ],
         [ '0', '1', 0.9 ],
         [ '1', '0', 0.6 ],
         [ '1', '1', 0.4 ]],[a]) 

e = ConditionalProbabilityTable(
        [[ '0', '0', 0.8 ],
         [ '0', '1', 0.2 ],
         [ '1', '0', 0.9 ],
         [ '1', '1', 0.1 ]],[b])

# State objects hold both the distribution, and a high level name.
A = State(a, name="A")
B = State(b, name="B")
E = State(e, name="E")

# Create the Bayesian network object with a useful name
model = BayesianNetwork("DS251_A2_Q5-2")

# Add the three states to the network 
model.add_states(A, B, E)

# Add edges which represent conditional dependencies, where the second node is 
# conditionally dependent on the first node (Monty is dependent on both guest and prize)
model.add_edge(A, B)
model.add_edge(B, E)

model.bake()

#a P(B|A)
round(model.predict_proba([{'B': '1'}])[0][8].parameters[0]['1'],4)