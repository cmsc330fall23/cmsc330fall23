# using project 3 code + graphviz script
# NFA 3 and 4 

trans = [(1,'b',6),
        (1,'c',2),
        (1,'a',5),
        (2,'b',5),
        (4,'a',5),
        (4,'b',3),
        (4,'epsilon',5),
        (5,'a',3),
        (5,'epsilon',6),
        (6,'a',4),
        (6,'a',3),
        (6,'epsilon',4)
        ]
b = Fsm(['a','b','c'],[1,2,3,4,5,6],1,[3],trans)
make_visual(b)

# nfa1 = Fsm(['a', 'b'], range(3), 0, [2], [
#     (0, 'a', 1), 
#     (1, 'b', 2), 
#     (1, 'b', 1), 
#     (2, 'a', 0), 
#     (0, 'epsilon', 2), 
# ])
# dfa1 = nfa_to_dfa(nfa1)
# dfa1.states.remove([])
# dfa1.transitions = [x for x in dfa1.transitions if x[0] != [] and x[2] != []]
# print(dfa1)
# make_visual(nfa1, "nfa3.png")
# # make_visual(dfa1)

nfa1 = Fsm(['a', 'b', 'c'], range(4), 0, [3], [
    (0, 'a', 1), 
    (0, 'epsilon', 2), 
    (1, 'b', 3), 
    (2, 'b', 3), 
    (2, 'a', 2), 
])
dfa1 = nfa_to_dfa(nfa1)
dfa1.states.remove([])
dfa1.transitions = [x for x in dfa1.transitions if x[0] != [] and x[2] != []]
print(dfa1)
make_visual(nfa1, "nfa3")
make_visual(dfa1, "dfa4")
