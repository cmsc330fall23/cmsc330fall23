# Project 3: Regular Expression Engine

Due: October 6, 2023 at 11:59 PM (late October 7: *10% penalty*, October 8: *20% penalty*, October 9: *30% penalty*)

Points: 35 public, 35 semipublic, 30 secret

**This is an individual assignment. You must work on this project alone.**

## Overview

In this project, you will implement algorithms to work with NFAs, DFAs, and regular expressions. In particular, you will implement 
- `accept` to see whether a string is accepted by a NFA
- `nfa_to_dfa` to convert an NFA to a DFA using subset construction
- `regex_to_nfa` to convert a regular expression to a NFA.

You will also implement several other helper functions to assist in these tasks.


The project is broken into two parts. All of these parts will be completed in the `fsm.py` file:
- Converting a NFA to a DFA
- Converting/working with Regular Expressions

### Ground Rules

To begin this project, you will need to commit any uncommitted changes to your local branch and pull updates from the git repository.

This is NOT a pair project. You must work on this project alone, as with most other CS projects. See the [Academic Integrity](#academic-integrity) section for more information. 

### Testing
You should test your project three different ways in the following order: 
1. Test locally using the provided public tests
2. Submit to Gradescope to see whether you're passing or failing the semipublics. 
3. Write student tests to best predict what you think the secret tests are.

Running the public tests locally can by done using the command below:

`python3 -m pytest test_public.py`. This command runs *only* the tests in `test_public.py`. 
If you would like to run your student tests simultaneously you can just type `pytest` with no arguments.

After running this, you will see the number of tests you're failing and why. Feel free to modify the test_public.py file in order to debug your code. If you wish to do so, you can always restore your `test_public.py` file to the default state by copying it from the git repository.

Submitting to gradescope can be done using the exact same method used for project 0. Add your changes, commit them, push them, and then enter the `submit` keyword.

You can write your own student tests in an attempt to predict the secret tests. Make a file called `test_student.py`. Put tests in this file following the format of the public.py file. Run the same command for running the public tests, but replace the file name with `test_student.py`.

### Submitting

First, make sure all your changes are pushed to github using the `git add fsm.py`, `git commit -m "message"`, and `git push` commands. You can refer to [my notes](https://bakalian.cs.umd.edu/assets/notes/git.pdf) for assistance. 

Next, to submit your project, you can run `submit` from your project directory.

The `submit` command will pull your code from GitHub, not your local files. If you do not push your changes to GitHub, they will not be uploaded to Gradescope.

### Academic Integrity

Please **carefully read** the academic honesty section of the course syllabus. **Any evidence** of impermissible cooperation on projects, use of disallowed materials or resources, or unauthorized use of computer accounts **will** be submitted to the Student Honor Council, which could result in an XF for the course or suspension or expulsion from the University. Be sure you understand what you are and what you are not permitted to do in regards to academic integrity when it comes to project assignments. These policies apply to all students, and the Student Honor Council does not consider lack of knowledge of the policies to be a defense for violating them. Full information is found in the course syllabus, which you should review before starting.

## Part 1: NFAs

This first part of the project asks you to implement functions that will help in creating the `nfa_to_dfa` algorithm. In particular, you will be asked to implement the *move* and *epsilon closure* functions [described in class](https://bakalian.cs.umd.edu/assets/notes/fa.pdf). You will also implement an `accept` function to determine whether a string is accepted by a given NFA; both *move* and *epsilon closure* may be handy here, too.

### FSM class

Before starting, you'll want to familiarize yourself with the class you will be working with.

The `Fsm` class is the class representing Finite State Machines. It is modeled after the formal definition of a NFA, a 5-tuple (Σ, Q, q0, F, δ) where:

1. Σ is a finite alphabet,
2. Q is a finite set of states,
3. q0 ∈ Q is the start state,
4. F ⊆ Q is the set of accept states, and
5. δ : Q × (Σ ∪ {ε}) → 𝒫(Q) is the transition function (𝒫(Q) represents the powerset of Q).

We translate this definition into a Python class in a straightforward way using object oriented programming:

```python
class Fsm:
  def __init__(self,sigma,states,start,final,transitions):
    self.sigma = sigma
    self.states = states
    self.start = start
    self.final = final
    self.transitions = transitions
```

A single transition in the `transition` instance variable of the Fsm class is in the form of a 3-tuple. For example:

```python
(0, 'c', 1)  #Transition from state 0 to state 1 on character 'c'
(1, 'epsilon', 0) #Transition from state 1 to state 0 on epsilon
```
These transitions are combined into a list in the Fsm class.

While the formal definition of a transition is a function that maps a state and character to a set of states, we will define transitions as 3-tuples that map a start state and a character to exactly one destination state. This means that that each edge in the NFA will correspond to a single transition in the list of transitions. This will make the syntax for defining NFAs cleaner and allow for a one-to-one mapping between elements of the transition list and edges in the NFA graph.

Python has a package called `graphviz`, which helps with visualization. You can install it through `pip install graphviz`. In your public and student tests, if you would like to visualize your NFA, you can do so by calling make_visual(filename,fsm,cleanup). `make_visual` is a function that we've provided for you in the visualizer.py file. The filename is the name of the file that you want to create, and it has type str. The fsm is your Fsm object, so it has type Fsm. cleanup has type bool, and you can either set it to True or False. Using graphviz is not required, but it can help you with your implementation. You can run `make_visual` directly from your test_public.py or test_student.py file. After you run `make_visual`, a folder called visual_output will be produced. If you set cleanup to True, you will only have the pdf file, while if you set cleanup to False, you will have both the gv and pdf files. For ease, you can set filename to 'output' and cleanup to True.

Please make sure that your transitions are a list of tuples of the form (src,letter,dest), with src and dest being states and letter being an element of the alphabet. For graphviz to work properly, src and dest must be either ints, strings, int lists, or string lists. For instance, a tuple could be (0,'a',1).

We also provide a `__str__` method for the class to help with debugging and seeing the actual values when you want to print your Finite State Machines.

An example NFA would be:

```python
nfa_ex = Fsm(['a'], [0, 1, 2], 0, [2], [(0, 'a', 1),(1, 'epsilon', 2)])
```

This looks like:

![NFA m](images/m_viz.png)

An example DFA would be:

```python
dfa_ex = Fsm(['a','b','c'], [0, 1, 2], 0, [2], [(0, 'a', 1), (1, 'b', 0), (1, 'c', 2)])
```

This looks like:

![NFA n](images/n_viz.png)

### Functions

Here are the functions you must implement:

#### `move(c,s,nfa)`
- **Description**: This function takes as input a NFA (`nfa`), a set of initial states (`s`), and a symbol (`c`). The output will be the set of states (represented by a list) that the NFA might be in after starting from any of the initial states in the set and making one transition on the symbol (or on epsilon if the symbol is `epsilon`). If the symbol is not in the NFA's alphabet, then return an empty list. You can assume the initial states are valid (i.e. a subset of the NFA's states).

- **Examples**:

  ```python
  move('a',[0],nfa_ex) = [1] #nfa_ex is the NFA defined above
  move('a',[1],nfa_ex) = []
  move('a',[2],nfa_ex) = []
  move('a',[0,1],nfa_ex)  = [1]
  move('epsilon',[1],nfa_ex) = [2]
  ```

- **Explanation**:
  1. Move on `nfa_ex` from `0` with `a` returns `[1]` since from 0 to 1 there is a transition with character `a`.
  2. Move on `nfa_ex` from `1` with `a` returns `[]` since from 1 there is no transition with character `a`.
  3. Move on `nfa_ex` from `2` with `a` returns `[]` since from 2 there is no transition with character `a`.
  4. Move on `nfa_ex` from `0` and `1` with `a` returns `[1]` since from 0 to 1 there is a transition with character `a`, but from 1 there is no transition with character `a`.
  5. Move on `nfa_ex` from `1` with `epsilon` returns `[2]` since from 1 to 2 there is an epsilon transition.

#### `e_closure(s,nfa)`
- **Description**: This function takes as input a NFA (`nfa`) and a set of initial states (`s`). It outputs a set of states that the NFA might be in after making ***zero or more*** epsilon transitions after starting from the initial states. You can assume the initial states are valid (i.e. a subset of the NFA's states).
- **Examples**:

  ```python
  e_closure([0],nfa_ex) = [0] #nfa_ex is the NFA defined above
  e_closure([1],nfa_ex) = [1,2]
  e_closure([2],nfa_ex)  = [2]
  e_closure([0,1],nfa_ex) = [0,1,2]
  ```

- **Explanation**:
  1. e_closure on `nfa_ex` from `0` returns `[0]` since you can only get to yourself from `0` on an epsilon transition.
  2. e_closure on `nfa_ex` from `1` returns `[1,2]` since from `1` you can get to `2` on an epsilon transition.
  3. e_closure on `nfa_ex` from `2` returns `[2]` since you can only get to yourself from `2` on an epsilon transition.
  4. e_closure on `nfa_ex` from `0` and `1` returns `[0,1,2]` since from `0` you can only get to yourself and from `1` you can get to `2` on an epsilon transition but from `2` you can only stay where you are.  

#### `accept(nfa,s)`
- **Description**: This function takes a NFA and a string and returns whether the NFA accepts the string.
- **Examples**:

  ```python
  accept(dfa_ex,"") = false  # dfa_ex is the DFA defined above, this is still an NFA. (Recall that all DFAs are NFAs. However, not all NFAs are DFAs. This function could technically take in any NFA).
  accept(dfa_ex,"ac") = true
  accept(dfa_ex,"abc") = false
  accept(dfa_ex,"abac") = true
  ```

- **Explanation**:
  1. accept on `dfa_ex` with the string "" returns `false` because initially we are at our start state, 0, and there are no characters to exhaust, so we end up at state 0, which is not a final state.
  2. accept on `dfa_ex` with the string "ac" returns `true` because from 0 to 1 there is an 'a' transition and from 1 to 2 there is a 'c' transition. Now, the string is empty, and we are in a final state. Thus, the NFA accepts "ac".
  3. accept on `dfa_ex` with the string "abc" returns `false` because from 0 to 1 there is an 'a' transition, but then to use the 'b' we go back from 1 to 0, and we are stuck at 0 because we need a 'c' transition, but there is only an 'a' transition.
  4. accept on `dfa_ex` with the string "abac" returns `true` because from 0 to 1 there is an 'a' transition, and then to use the 'b' we go back from 1 to 0. Then, we take an 'a' transition to go to state 1 again and then finally from 1 to 2 we exhaust our last character 'c' to make it to our final state. Since we are in a final state, the NFA accepts "abac".

---

Our goal now is to implement the `nfa_to_dfa` function. It uses the subset construction to convert an NFA to a DFA. For help with understanding Subset Construction, you can look at the [lecture notes](https://bakalian.cs.umd.edu/assets/notes/fa.pdf). We recommend you implement `move` and `e_closure` before starting working on the NFA to DFA algorithm, since they are used in the subset construction.

Remember that every DFA is also a NFA, but the reverse is not true. The subset construction converts a NFA to a DFA by grouping together multiple NFA states into a single DFA state. Notice that each DFA state is now a set of states from the NFA. The description will use "DFA state" to mean a set of states from the corresponding NFA.

#### `nfa_to_dfa(nfa)`
- **Description**: This function takes as input a NFA(`nfa`) and converts it to an equivalent DFA. The language recognized by a NFA is invariant under `nfa_to_dfa`. In other words, for all NFAs `nfa` and for all strings `s`, `accept nfa s = accept (nfa_to_dfa nfa) s`.

## Part 2: Regular Expressions
For the last part of the project, you will implement code that builds a NFA from a regular expression. 

You will create functions that build a NFA based on the things we learned in class.

Here are the functions you must implement:

#### `def char(string):` 
-  **Description**: Takes in a character and returns a NFA (a FSM object) that accepts the string and only that string.
- It may help to create a global variable and increment it every time a state is created to ensure that each new state you create is different. You may use the `fresh` function we have provided to help, but you are not required to use it.
-  **Examples**:

  ```python
  char('a') = Fsm(['a'], [0, 1], 0, [1], [(0,'a',1)])  # You can create any Fsm object that accepts the string 'a' and only that string.
  ```

#### `def concat(nfa1, nfa2):`
-  **Description**: Takes in two NFA's and returns a new NFA that is the concatenation of the two NFA arguments.

#### `def union(nfa1, nfa2):`
-  **Description**: Takes in two NFA's and returns a new NFA that is the union of the two NFA arguments.

#### `def star(nfa):`
-  **Description**: Takes in a NFA and returns a new NFA that has the kleene closure applied to it.

[lecture slides]: https://bakalian.cs.umd.edu/330/schedule
[lecture notes]: https://bakalian.cs.umd.edu/330/schedule 
