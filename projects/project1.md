# Project 1: Introduction to Python
Due: September 10th, 2023 at 11:59 PM <br>
This project has four parts. You can do the parts in any order, but it's recommended to start with part 1 and chronologically move to part 4. The grading for this project will be spread across public, semipublic, and secret tests. The breakdown is public (40%), semipublic (40%) and secret (20%). As a reminder:

`publics`: You have the code we use for these tests, and you can run these tests locally or on gradescope.<br>
`semipublics`: You don't have the code for these tests, but you know if you are failing them on gradescope.<br>
`secrets`: You don't have the code, and you don't know if you're failing them until grades are released.<br>

You may *not* import any packages other than `from functools import reduce`.

## Part 1: Python Basics
All code for part 1 should be located in a file called `basics.py`. If the file does not have the name `basics.py`, the testing infrastructure will not be able to grade your work. 

Implement the functions below. Ensure each function prototype matches the one we give:
#### `isPalindrome(n)`
- **Description**: Returns `true` if `n` is a palindrome and `false` otherwise. A palindrome is the same read forward and backward.
- **Type**: `(Integer) -> Bool`
- **Assumptions**: `n` is non-negative; `n` will not be provided with any leading 0s.
- **Hint**: It may be easier to do this after converting the provided integer to a String.
- **Examples**:
  ```py
  isPalindrome(0) == True
  isPalindrome(1) == True
  isPalindrome(10) == False
  isPalindrome(101) == True
  isPalindrome(120210) == False

#### `nthmax(n, a)`
- **Description**: Returns the `n`th largest element in the array `a` or `None` if it does not exist. The largest element is specified using n = 0. Treat duplicated values seperately.
- **Type**: `(Integer, Array) -> Integer or None`
- **Assumptions**: `n` is non-negative.
- **Examples**:
  ```py
  nthmax(0, [1,2,3,0]) == 3
  nthmax(1, [3,2,1,0]) == 2
  nthmax(2, [7,3,4,5]) == 4
  nthmax(5, [1,2,3]) == None

#### `freq(s)`
- **Description**: Returns a one-character string containing the character that occurs with the highest frequency within 's'. If `s` has no characters, it should return the empty string.
- **Type**: `String -> String`
- **Assumptions**: Only one character will have the highest frequency (i.e. there will be no "ties").
- **Examples**:
  ```py
  freq("") == ""
  freq("aaabb") == "a"
  freq("bbaaa") == "a"
  freq("ssabcd") == "s"
  freq("a12xxxxxyyyxyxyxy") == "x"

## Part 2: Data Structure Basics + Code Control
All code for part 2 should be located the same file for part 1 (`basics.py`).

#### `zipHash(arr1, arr2)`
- **Description**: Returns a dict that maps corresponding elements in `arr1` and `arr2`, i.e., `arr1[i]` maps to `arr2[i]`, for all i. If the two arrays are not the same length, return `None`.
- **Type**: `(Array, Array) -> Dict or None`
- **Examples**:
  ```py
  zipHash([], []) == {}
  zipHash([1], [2]) == {1: 2}
  zipHash([1, 5], [2, 4]) == {1: 2, 5: 4}
  zipHash([1], [2, 3]) == None
  zipHash(["Mamat", "Hicks", "Vinnie"], ["prof", "prof", "TA"]) == {"Mamat": "prof", "Hicks": "prof", "Vinnie": "TA"}
  ```

#### `hashToArray(hash)`
- **Description**: Returns an array of arrays; each element of the returned array is a two-element array, where the first item is a key from the hash and the second item is its corresponding value. The entries in the returned array must be in the same order as they appear in `hash.keys`.
- **Type**: `(Hash) -> Array`
- **Examples**:
  ```py
  hashToArray({}) == []
  hashToArray({"a": "b"}) == [["a", "b"]]
  hashToArray({"a": "b", 1: 2}) == [["a", "b"], [1, 2]]
  hashToArray({"x": "v", "y": "w", "z": "u"}) == [["x", "v"], ["y", "w"], ["z", "u"]]
  ```

#### `maxLambdaChain(init, lambdas)`
- **Description**: Takes a list of lambda expressions and decides to either apply each lambda
or not to maximize the final or not. For example, if I have a list of lambda expressions:
`[LA, LB, LC]` and an initial value `x`, then I take the maximum value
of
   + `x`
   + `LA(x)`
   + `LB(LA(x))`
   + `LC(LB(LA(x)))`
   + `LC(LA(x))`
   + `LB(x)`
   + `LC(LB(x))`
   + `LC(x)`
You may assume each lambda has type `Integer -> Integer`.
- **Type**: `(Integer, Array) -> Integer`
- **Hint**: There is an elegant recursive solution.
- **Examples**:
  ```py
  maxLambdaChain(2,[(lambda x: x + 6)]) == 8
  maxLambdaChain(2,[(lambda x: x + 4), (lambda x: x * 4)]) == 24
  maxLambdaChain(-4,  [(lambda x: x * 4), (lambda x: x + 3)]) == -1
  ```

## Part 3: Object Oriented Programming
For this part, edit the `roster.py`. You will be making a `roster` class that
keeps track of a list of `Person`s. There are 2 types of `Persons`: `Staff` and
`Student`s. The following describes the 4 classes you need to make along with 
any mandatory associated methods. You may add other classes and methods if you
need them. All classes should be written in `roster.py`

## Person
 This is the superclass of `Staff` and `Student`. Every person has a `name`, 
 and `age` attribute. Every `Person` should also have the following 
 methods
 
#### `__init__(name,age)`
- **Description**: creates a Person with `name` and `age`. 
- **Type**: `(String, Integer)-> self`
- **Examples**:
  ```py
  Person('Cliff',84)
  ```

#### `get_age`
- **Description**: Returns the age of the person
- **Type**: `None-> Integer`
- **Examples**:
  ```py
  clyff = Person('Cliff', 84)
  clyff.get_age() == 84
  ```

#### `set_age(x)`
- **Description**: changes the age of the person. You may assume that any age 
is valid. Returns `self`
- **Type**: `Integer -> self`
- **Examples**:
  ```py
  clyff = Person('Cliff', 84)
  clyff.set_age(42)
  clyff.get_age() == 42
  ```

## Student

This is a subclass of a `Person`. Each student has a `grade` attribute.
Every `Student` should also have the following methods

#### `__init__(name,age, grade)`
- **Description**: creates a Student with `name`, `age` and `grade` 
- **Type**: `(String, Integer, Float)-> self`
- **Examples**:
  ```py
  Student('Cliff',16,72.5)
  ```

#### `get_grade`
- **Description**: Returns the grade of the student 
- **Type**: `None-> Float`
- **Examples**:
  ```py
  clyff = Student('Cliff',16,72.5)
  clyff.get_grade() == 72.5
  ```

#### `change_grade(x)`
- **Description**: changes the grade of the student. You may assume that any 
grade is valid. Returns `self`
- **Type**: `Float-> self`
- **Examples**:
  ```py
  clyff = Student('Cliff', 84, 50.0)
  clyff.change_grade(42.0)
  clyff.get_grade() == 42.0
  ```

## Staff

This is a subclass of a `Person`. Each staff member has a `position` attribute
Every `Staff` member should also have the following methods

#### `__init__(name, age, position)`
- **Description**: creates a Student with `name`, `age` and `position` 
- **Type**: `(String, Integer, String)-> self`
- **Examples**:
  ```py
  Staff('Cliff',16,'Professsor')
  ```

#### `get_position`
- **Description**: Returns the position of the staff member 
- **Type**: `None-> String`
- **Examples**:
  ```py
  clyff = Staff('Cliff',16,"TA")
  clyff.get_position() == "TA"
  ```

#### `change_position(newPosition)`
- **Description**: changes the position of the student. You may assume that 
`newPosition` is always valid. Returns `self`
- **Type**: `String -> self`
- **Examples**:
  ```py
  clyff = Staff('Cliff', 84, "TA")
  clyff.change_position("Head TA")
  clyff.get_position() == "Head TA"
  ```

## Roster

This will hold all the `Person`s. You should make your own `__init__` method..

#### `add(person)`
- **Description**: Adds the person to the roster. 
- **Type**: `Person -> None`
- **Examples**:
  ```py
  roster = Roster()
  roster.add(Staff('Cliff', 84, 'Professor'))
  ```

#### `size`
- **Description**: Returns how many people are in the roster 
- **Type**: `None -> Integer`
- **Examples**:
  ```py
  roster = Roster()
  roster.size() == 0
  roster.add(Person('Cliff', 84, 'Professor'))
  roster.size() == 1
  ```

#### `remove(Person)`
- **Description**: remove the person from the roster. You may assume everyone 
in the roster is unique. If the person is not in the roster, do nothing.
- **Type**: `Person -> None`
- **Examples**:
  ```py
  roster = Roster()
  clyff = Person('Cliff', 84)
  roster.add(clyff)
  roster.remove(clyff)
  roster.size() == 0
  ```

#### `get_person(name)`
- **Description**: get the person with `name` in the roster. You may assume that
everyone in the roster has a unique name. If the person is not in the roster, 
return None.
- **Type**: `String-> Person`
- **Examples**:
  ```py
  roster = Roster()
  cliff = Person('Cliff', 84)
  roster.add(cliff)
  cliff == roster.get_person('Cliff')
  ```

#### `map`
- **Description**: Takes in a function of type `Person -> Person` and applies it to 
every person in the roster.
- **Type**: `None`
- **Examples**:
  ```py
  roster = Roster()
  roster.add(Person('Cliff', 84))
  roster.add(Person('Clyff', 42))
  roster.map(lambda person: person.set_age(52))
  roster.get_person('Cliff').get_age() == 52
  roster.get_person('Clyff').get_age() == 52
  ```

## Part 4: Higher Order Functions
What are they?
- Basically use functions as parameters for other functions
- Able to assign functions to variables

What's the point?
- More concise code
- Cleaner code
- Abstraction

Implement the functions below using higher order functions. All code for these functions should be in their own file called `hof.py`. There are a few function headers inside the src file `hof.py` which are not required, but may be useful for the required functions. The only required functions for the `hof.py` file are the ones listed below. 

### HOF and Lambda Practice

You are not required to use Higher Order Functions to complete this section, however **it is recommended to practice programming with HOF in mind**. Not doing so will hinder you in further projects.

#### `uniq(lst)`
- **Description**:   Given a list, returns a list with all duplicate elements removed. Order matters.
- **Hint**: `is_present()` and `count_occ()` may be helpful to implement and use when designing `uniq()`
- **Examples**:
    ```py
    uniq([1,2,1,2]) == [1,2]
    uniq([4,3,7,6,7]) == [4,3,7,6]
    uniq([4,3,2,1]) == [4,3,2,1]
    ```

#### `find_max(matrix)`
- **Description**: given a list of lists find the maximum. You may assume the inputs are non-negative ints.
- **Examples**:
    ```py
    find_max([[1,2],[3,4],[5,6]]) == 6
    find_max([[1,1],[1],[1]]) == 1
    ```

#### `count_ones(matrix)`
- **Description**: given a matrix, count how many 1s are in the matrix
- **Examples**:
    ```py
    count_ones([[1,1],[1],[1]]) == 4
    count_ones([[],[3],[0]]) == 0
    ```

#### `addgenerator(x)`
- **Description**: return a lambda function that adds x to its parameter
- **Examples**:
    ```py
    addgenerator(4)(5) == 9
    addgenerator(1)(5) == 6
    ```

#### `apply_to_self()`
- **Description**: return a lambda function that takes in 2 parameters. The first is an element and the second is a function. The body of the lambda function should add the element to the application of the function to the element. You may assume that the elementis an int
- **Examples**:
    ```py
    apply_to_self()(2,lambda x: x + 1) == 5 # 2 + (2 + 1)
    apply_to_self()(4,lambda x: -x) == 0 # 4 + (-4)
    ```

#### `map2(matrix,f)`
- **Description**: write a function that is similar to `map` but works on lists of lists
- **Examples**:
    ```py
    map2([[1,2,3],[4,5,6]],lambda x: -x) == [[-1,-2,-3],[-4,-5,-6]]
    map2([[1,2,3],[4,5,6]],lambda x: 0) == [[0,0,0],[0,0,0]]
    ```

## Testing & Submitting

Running the public tests locally can be done by running the following command from the root directory of project 1: `python3 -m pytest`. This command indicates the number of tests you're failing and why. Feel free to modify the public.py file in order to debug. If you make too many modifications you can always restore to the default state by copying from the git repository.

Submitting to gradescope can be done using the exact same method used for project 0. Stage (Add), commit, then push your changes to your remote repo. Run the `submit` keyword to send your changes to gradescope.

You can write your own tests by following the framework within the tests directory. Just make a python file which follows the same style as the test_public.py file. Execute it using the same `pytest` command shown above.
