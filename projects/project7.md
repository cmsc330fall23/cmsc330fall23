# Project 7: Rust Basics
## Due: Wed 29-Nov, 2023 at 11:59 pm
## Points: 100 public
- 65 for Problem 1 spread across several functions
- 35 for Problem 2 for a small command line program

## FAQ: TBD (see pinned Piazza posts)

## Overview
This project introduces basic Rust techniques. 

The first problem builds a number of independent functions which rise
moderately in complexity.  Early functions deal with basic syntax and
iteration through Rust's Slices like type `&[i32]`.  Later functions
will require handling of references and dealing with modest ownership
issues that may involve borrowing via the reference creation operator
`&` or cloning data with that method supported.

The second problem builds a small command line program which apes the
behavior of the classic `wc` UNIX utility: it counts the characters,
words, and lines in an input file. This will give a chance to build a
command line program and deal with basic file input in Rust.

## Code Pack Files
The following files are distributed in the codepack.

| File                  | State    | Description                                |
|-----------------------|----------|--------------------------------------------|
| `project7/`           | Provided | Project root                               |
| `Makefile`            | Provided | Supplementary build file, try `make help`  |
| `Cargo.toml`          | Provided | Options for the project                    |
| `README.md`           | Provided | Project description                        |
|                       |          |                                            |
| `src/prob1_basics.rs` | EDIT     | Problem 1 functions to complete            |
| `src/bin/prob2_wc.rs` | EDIT     | Problem 2 executable to complete           |
|                       |          |                                            |
| `src/bin/cmd_args.rs` | Provided | Sample file demoing command line arguments |
| `src/bin/readfile.rs` | Provided | Sample file demoing file reading           |
|                       |          |                                            |
| `tests/test_prob1.rs` | Testing  | Unit Tests for Problem 1                   |
|                       |          | Try `make test-prob1`                      |
| `test_prob2_wc.sh`    | Testing  | Overview testing script for Problem 2      |
|                       |          | Try `make test-prob2`                      |
|                       |          |                                            |
| `test_prob1.org`      | Testing  | Point totaling for Problem 1               |
| `test_prob2.org`      | Testing  | Point totaling for Problem 2               |
| `test_post_filter`    | Testing  | Used during points tallying                |
| `test-data/*`         | Testing  | Test input files                           |
| `testy`               | Testing  | Testing framework for totaling scores      |

## Cargo Commands
The standard method to build and run tests with Rust's Cargo tool is
as follows:
```sh
## only build code, show compiler errors
>> cargo build
   Compiling project7 v0.1.0 (./330-F2023/projects/p7-rust/p7)
    Finished dev [unoptimized + debuginfo] target(s) in 0.79s

## build code and tests and then run all tests
>> cargo test
   Compiling project7 v0.1.0 (/home/kauffman/Dropbox/teaching/330-F2023/projects/p7-rust/p7)
...
     Running tests/test_prob1.rs (target/debug/deps/test_prob1-7c1ed0b0312b59c1)

running 16 tests
test test_circulant1 ... ok
test test_circulant2 ... ok
...
test test_count_words2 ... ok

test result: ok. 16 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s
```

This is standard for development environments but lacks a few useful
features such as point totaling and testing of executable that may be
part of the project.

## Building the Project and Running Tests
Since Cargo lacks point totaling and easy testing of executable, this
project layers a `Makefile` on top of it with a few other testing
files. These can be accessed via the standard `make` utility which you
may need to install. A demo:
```sh
>> make help
Typical usage is:
  > make                          # build all programs
  > make test                     # run all tests
  > make test-prob1               # run test for problem 1
  > make test-prob2               # run test for problem 2
  > make clean-tests              # remove test-results/ directory
  > make clean                    # remove build files

LINUX ONLY (makes use of testy script which fails on MacOS
  > make ltest                    # run all tests and show scores, linux only
  > make ltest-prob1              # run problem 1 tests and show score, linux only
  > make ltest-prob2              # run problem 2 tests and show score, linux only
  > make ltest-prob2 testnum=5    # run problem 2 test #5 only, linux only

>> make test-prob1
cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
cargo test --test test_prob1
    Finished test [unoptimized + debuginfo] target(s) in 0.02s
     Running tests/test_prob1.rs (target/debug/deps/test_prob1-8c4fed3e3a54c66a)

running 16 tests
test test_circulant1 ... ok
test test_circulant2 ... ok
test test_circulant3 ... ok
...
test test_count_words1 ... ok
test test_count_words2 ... ok

test result: ok. 16 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

>> make test-prob2
./test_prob2_wc.sh

=============== PROBLEM 2 TESTS ===============
BUILDING PROGRAMS
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
...
EXPECTED AND ACTUAL OUTPUT DIFFER, TEST FAILURES LIKELY
Examine the above side-by-side diff, look for | < > symbols
in the middle which indicate differnces between the Expected
and Actual output
```

The command `make test-prob1` will build and run tests for problem 1
and report the point totals for it. Likewise `make test-prob2` will
test problem 2 and `make test` will run all tests.

On Linux systems, you may also run `make ltest` to run all tests just
as they would on Gradescope which will show your overall scores for
Problems 1 and 2 along with additional information on test
failures. Unfortunately MacOS and Windows cmd.exe are incompatible
with the scripts used for this.

## Ground Rules
As before, this is an individual assignment. You only receive help on
the project from staff members associated with the course.

Generally you may use functionality in Rust's standard library and the
external Regex crate which will be downloaded as part of the first
project build. However, use of an existing function or package that
would complete a required function or program in with no effort from
the student is prohibited under penalty of loss of all credit on the
project.  That is: do the work.

Guidance is given on techniques to use in each of the problems so keep
a copy of the README close.

# Problem 1: Basic Functions in `src/prob1_basics.rs`

## `gauss`
As the story goes, [young Friedrich Gauss was tasked to add up numbers
1 to
100](https://www.americanscientist.org/article/gausss-day-of-reckoning)
and had it done in a snap.  Write a function to do the same for an
arbitrary stopping integer.  The input type for the function is an
`i32`, a 32-bit integer referred to almost everywhere else as an
`int`.

```rust
pub fn gauss(n: i32) -> i32;
/// Returns the sum 1 + 2 + ... + n
/// 
/// If n is less than 0, return -1
/// 
/// May use either a fixed equation to calculate the answer or an
/// iterative approach (though Gauss himself would likely prefer the
/// former...)
///
/// EXAMPLES:
/// gauss(5)  -> 15
/// gauss(10) -> 55
/// gauss(-2) -> -1
```

## `in_range`
Count elements in a range. 
```rust
pub fn in_range(slice: &[i32], lo: i32, hi: i32) -> i32
/// Returns a count of elements in `slice` that satisfy:
///   lo <= x <= hi
/// Uses an iterator over the slice to ensure all elements are visited.
///
/// EXAMPLES:
/// in_range([5,2,1,3,9], 2, 5)  -> 3
/// in_range([5,2,1,3,9], 3, 4)  -> 1
/// in_range([5,2,1,3,9], 2, 10) -> 4
/// in_range([], 2, 10)          -> 0
```

The data type in this case is Rusts [*Slice
type*](https://doc.rust-lang.org/book/ch04-03-slices.html#other-slices)
notated here as `&[i32]` for
- `[..]` to indicate that it is a slice 
- `i32` to indicate the elements of the slice are `i32` integers
- `&` to indicate this is a reference to a slice (almost all slices
  are references)

Slices serve a similar place to arrays in other languages. They are of
fixed length and one can access their length via `slice.len()`.  They
also have a wide [variety of
methods](https://doc.rust-lang.org/std/primitive.slice.html)
associated with them. One aspect that they have in common with
containers in Python and Java is their "iterability" as in:
```rust
fn printall(slice: &[i32]){
  for &x in slice {
    println!("x: {}",x);
  }
}
```
Several other Rust data types such as Vectors have this property. 

Keep in mind as well that rust defaults all `let` bound variables to
immutable by default so you'll likely need to set up mutability. 

## `mean`
```rust
pub fn mean(slice: &[f64]) -> Option<f64>
/// Calculates and returns the mean of elements in `slice` of floating
/// point values. To handle empty slices, this function returns an
/// Option: None for empty slices, and Some(mean) for filled slices.
///
/// EXAMPLES:
/// mean([])                     -> None
/// mean([10.0, 5.0, 7.0, 20.0]) -> Some(10.5)
/// mean([-10.0, 3.0, 2.0])      -> Some(-1.6666)
```

This function will have nearly identical structure to the previous one
for its iteration pattern.  The catches are to add just a little
checking for 0-length slices and to get used to the Option type which
is identical in form and use to OCaml's option.

### `subset`
```rust
pub fn subset<T>(slicea: &[T], sliceb: &[T]) -> bool
  where T: PartialEq<T>         // allows comparisons via ==
/// Returns true if `slicea` is a subset of `sliceb` and false
/// otherwise. The function is generic so works with slices of any
/// type. The slices are not ordered so must be searched sequentially.
/// 
/// EXAMPLES:
///   subset([1,3,2], [1,2,3,4,5]) -> true
///   subset([1,3,2], [1,3,4,5])   -> false
///   subset(["a","c","d","c"], ["d","c","a"])     -> true
///   subset(["a","c","d","c"], ["d","c","a","r"]) -> true
///   subset(["a","q","d"],     ["d","c","a","r"]) -> false
///
/// NOTE: Utilizing certain methods of slices may lead to shorter code
/// by letting methods detect whether elements are contained or not.
```

Examining the prototype for `subset()` carefully you'll see that it
has a type parameter `<T>`. This makes the function generic: it can
work on any type of slice as shown in the examples. There is a
constraint on `T` however: it must implement certain methods which are
described in the `PartialEq` trait (traits are collections of methods
similar to Java's interfaces).  The essence of `PartialEq` is that it
allows two data to compared for equality via `a == b`. Types like
integers and strings have this property so will work with `subset()`

To complete `subset()` you'll need to check whether all elements of
the left `slicea` exist in the right `sliceb`.  There is no order to
either set so a linear search is in order. You may do this manually or
explore methods of slices that may lower the number of lines of code
you need to write.


### `to_binstring`
```rust
pub fn to_binstring(num: u32) -> String
/// Return a string showing the binary digits of the given unsigned
/// (positive) integer. Calculates the binary digits through repeated
/// division by 2 where the remainders become the digits in the binary
/// number. A survey of this method is here
/// https://www.cuemath.com/numbers/decimal-to-binary/
///
/// While converting, pushes digits of "0" or "1" into a container
/// type, vector being a good choice.  These digits need to be
/// reversed at the end of the computation (last digit found is most
/// significant, leftmost bit) so visits the digits in reverse order
/// in the container appending them to a String which is ultimately
/// returned.
///
/// No leading zeros are provided so the left-most character is always
/// a 1 EXCEPT in the special case of decimal value 0 which should
/// return the string "0".
/// 
/// EXAMPLES:
/// to_binstring(  0) ->         "0"
/// to_binstring(  2) ->        "10"
/// to_binstring(  9) ->      "1001"
/// to_binstring( 32) ->    "100000"
/// to_binstring(510) -> "111111110"
```

The function above is meant to convert a number to a string
representing its binary equivalent.  Before engaging with the code,
it's a good idea to work a few examples by hand to make sure you have
a solid algorithm to use. The easiest one to implement (and therefore
the recommended one) is to repeatedly divide by 2 and track remainders
which are then reversed. Here is a brief example:

*Convert 124 to base 2*:
```text
124 / 2 = 62   rem 0
 62 / 2 = 31   rem 0
 31 / 2 = 15   rem 1
 15 / 2 = 7    rem 1
  7 / 2 = 3    rem 1
  3 / 2 = 1    rem 1
  1 / 2 = 0    rem 1

Remainders in revers order:
1111100 which is 124
```
Take note of the termination criteria (quotient is 0) and that the
remainders are the digits of the binary number. 

Also take note that after the digits are accumulated, you'll need to
reverse them. This is usually done by pushing to the end of a vector
or string then visiting the elements in reverse order. Doing so yields
a Linear time algorithm.

Or you can implement a quadratic algorithm that inserts at the
beginning of your data structures... *like a chump.*

You'll want to acquaint yourself with the `String` and `Vector` types
that Rust provides which have methods like `push_str(x) / push(x)` to
take on to their ends and are iterable.

## `circulant`
```rust
pub fn circulant<T>(r0_slice: &[T]) -> Vec<Vec<T>>
  where T:Clone                 // elements have .clone() for deep copying
/// Construct a circulant matrix (2D vector) from the given
/// slice. Briefly a circulant matrix has row i rotated left by i
/// elements with row 0 being identical to the parameter r0_slice. A
/// vector or rows is allocated and each row is constructd as a
/// rotation left by i indices from the 0th row. The function is
/// generic and accepts any type that can be Cloned elements from
/// r0_slice must have clone() invoked on them to get a memory
/// distinct copy of them.
///
/// EXAMPLES:
/// 
/// circulant(&[1,2,3]) ->
///  [[1,2,3],
///   [2,3,1],
///   [3,1,2]]
///
/// circulant(&["a","b","c","d"]) ->
///  [["a","b","c","d"]
///   ["b","c","d","a"]
///   ["c","d","a","b"]
///   ["d","a","b","c"]]
```

Note again that `ciculant()` is generic and will work on any type so
long as the elements can be `.clone()`'d as dictated by the `Clone`
trait.  The typical algorithm to complete this is to allocate a Vector
of rows, then build each row of the matrix by cloning elements from
the input slice into a row vector and finally adding the completed row
to vector of all rows.  There is a bit of trickiness with getting the
iteration pattern right to shift elements in each row but with a
little finagling this one will not be too bad.

## `count_words`
```rust
pub fn count_words(text: &String) -> i32 
/// Returns a count of the number of "words" in `text`. The notion of
/// a word is a series of non-whitespace characters, (whitespace is
/// space, tab, newline). Regular expressions may be used for counting
/// words or character-by-character iteration to count whitespace
/// transitions. In either case, iteration through the string will be
/// required, either by regex match by direct iteration on the
/// characters.
/// 
/// NOTE: The Regular expression "crate" is marked as a dependency for
/// this project so will be downloaded HOWEVER you will need to add an
/// appropriate "use" statement to access its functionality here.
/// 
/// EXAMPLES:
/// count_words( &String::from("hello world"))                          -> 2
/// count_words( &String::from("       "))                              -> 0
/// count_words( &String::from("ALL ... NON - whitespace !! "))         -> 6
/// count_words( &String::from("tabs\tor spaces\tor\ttabs\tor spaces")) -> 7
```

A classic use of regular expressions is to iterate across some notion
of words. An easy definition of a "word" is a contiguous sequence of
non-whitespace characters. As the doc comment indicates, you may
attempt the problem by either
- Using the Regular expression crate that Rust provides which will
  require searching out its API and adapting what you've learned about
  regexs to this situation
- Iterating over the characters and doing some manual checking. This
  will be tedious but since the difference is merely whitespace vs
  not, it is feasible to hand code this. Just expect to make some
  mistakes in your first attempts.

Note: the input type is `&String`, a string reference. This function
would probably be better specified as a string slice as in `&str` as
this would make it more flexible but this was only realized after all
the test cases were written. So it goes...

# Problem 2: Word Count on Files in `src/bin/prob2_wc.rs`
Expanding on the last function in the basics which counted words in a
string, this problem will have you implement a small command line
program that approximates the functionality of the classic `wc` UNIX
utility that prints the number of characters, words, and lines in a
file. For those unacquainted, `wc` works as follows:
```
>> wc test-data/bruce.txt 
 2 17 91 test-data/bruce.txt

#  2 lines
# 17 words
# 91 characters

>> wc test-data/howl.txt 
  145  2909 17521 test-data/howl.txt

#   145 lines
#  2909 words
# 17521 characters
```

## Create and Run a Main Function
In the file `src/bin/prob2_wc.rs` create a `main ()` function. This
should allow you to use the following cargo commands to experiment
with it.
```sh
# with command line arg of 'test-data/bruce.txt'
>> cargo run --bin prob2_wc -- test-data/bruce.txt 
...

# no command line arg to test functionalty when it is missing
>> cargo run --bin prob2_wc -- 
...

# with --quiet don't print cargo build messages
>> cargo run --quiet --bin prob2_wc -- test-data/bruce.txt 
...
```
While more cumbersome that just running an `a.out`, it is the
prescribed method to stay compatible with cargo which buries built
executables several layers deep in the project directory structure.

Interactive experimentation will be helpful as you develop your
program. 

## Command Line Handling
Examine the provided `src/bin/cmd_args.rs` which demonstrates how to
access commandline arguments in Rust. This is necessary in `prob2_wc`
as the file to counted comes from the command line. Experimenting with
this program is a good idea and can be done using a similar cargo
command as above:
```sh
>> cargo run --quiet --bin cmd_args -- abc 123 you and me
arg[0]: target/debug/cmd_args
arg[1]: abc
arg[2]: 123
arg[3]: you
arg[4]: and
arg[5]: me
6 total args
```

## Opening and Reading Files Line-by-Line
A common tactic for handling input files is to read them one line at a
time. This is often done in Rust via the `BufReader` type and is
demonstrated in the provided `src/bin/readfile.rs` program.  It demos 
several ways as well that files are opened and checked for errors as
well as how to iterate through lines of a file printing each line in
turn. Again, experimenting with this program will allow you to adapt
its techniques to solve problem 2:
```sh
>> cargo run --quiet --bin readfile -- 
readlines1():
1: Four score and seven years ago our fathers brought forth on this continent, a
2: new nation, conceived in Liberty, and dedicated to the proposition that all men
3: are created equal.
4: 
5: Now we are engaged in a great civil war, testing whether that nation, or any
...
```

Pay close attention to several aspects of handling files demonstrated
in `readfile.rs`
- Opening files returns Rusts `Result` type, with variants of `Ok` and
  `Err` indicating success and failure.  These must be handled in some
  way. Several options including `match` statements are demonstrated
  in `readfile.rs`.
- Unlike in `readfile.rs`, there are some specific non-`panic!`
  expectations for `prob2_wc` when a file can't be opened which are
  described in the next subsection.
- Reading lines may also fail yielding `Ok/Err` results. Handling for
  this is also demonstrated and should be mimicked.

**NOTE**: when reading line-by-line with `BufReader`, newline
characters are always **chopped**. This means that if you are trying
to count characters (and you are) you'll need to add one for each line
to account for the omitted `\n`.  At least, this is the case when
handling UNIX files which are the provided test files. Windows users
that open up those text files may inadvertently convert them to DOS
format which uses 2 characters per line break and is likely to break
the tests. Be forewarned on all accounts: add 1 char per line and
avoid converting files to DOS text format.

## Graceful Exiting
In the event that no command line is provided OR that a file cannot be
opened, `prob2_wc` should exit gracefully using the `exit(num)`
function from the standard rust libraries. This function has already
been `used`ed at the top of the `prob2_wc.rs` file so can be used without
qualifying its crate location.

The required messages for failure are as follows:
```sh
>> cargo run --quiet --bin prob2_wc -- 
usage: target/debug/prob2_wc <filename>


# error when unable to open a file
>> cargo run --quiet --bin prob2_wc -- no-such-file.txt
Couldn't open file no-such-file.txt: No such file or directory (os error 2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ||||||||||||||||||||||||||||||||||||||
Required messsage                    Reason provied by Err(reason)
```

The second message has two parts: the left part is from `prob_wc`
while the right part is part of the `Err()` variant that is returned
when a file fails to open. Print them together when this occurs.

## Counting Words
It is slightly trickier to count words than lines and
characters. However, you *may* have completed a function that does
just that recently and it *may* be a good idea to make use of it here.

Accessing a function in `prob2_wc.rs` from another part of the project
can be done with a `use` statement. Experiment a little using the
following basic pattern:

```rust
use project_name::file_name:function_name;
```
Technically speaking these are crate and module names, not project and
function, but the similarities are enough.

Once this you have access to your function from problem 1, use it to
count words on each line that is read.

## Output Formatting
After counting lines, words, and characters. Print a message at the
end of the program indicating the counts and the filename like the
following examples:
```
>> cargo run --quiet --bin prob2_wc -- test-data/dijkstra.txt
  40  271 1633 test-data/dijkstra.txt
  |    |    |    |
line word char  filename
```

Each of line/word/char are 4 wide minimum with right alignment and
whitespace padded on the left. If this sounds intimidating, you'll
find Rust's format strings are useful: try using something like
```rust
println!("{:4}",anumber);
```
and adapt as needed. While some of the examples have more than 4
digits in their counts, we're not aiming for total beauty, just
awareness that format strings are useful.

# Submitting
First, make sure all your changes are pushed to Github using the `git
add`, `git commit`, and `git push` commands.

Next, to submit your project, you can run `submit` from your project
directory.

The `submit` command will pull your code from GitHub, not your local
files. If you do not push your changes to GitHub, they will not be
uploaded to gradescope.

NOTE: All submissions are subject to manual review. If it is
determined that code passed tests cases due to their hard-coding
behavior to match test case expectations, credit will be deducted with
additional penalties. As ever: Do the work.

# Academic Integrity

Please **carefully read** the academic honesty section of the course
syllabus. Academic dishonesty includes posting this project and its
solution online like a public github repo. **Any evidence** of
impermissible cooperation on projects, use of disallowed materials or
resources, or unauthorized use of computer accounts, **will be**
submitted to the Student Honor Council, which could result in an XF
for the course, or suspension or expulsion from the University. Be
sure you understand what you are and what you are not permitted to do
in regards to academic integrity when it comes to project
assignments. These policies apply to all students, and the Student
Honor Council does not consider lack of knowledge of the policies to
be a defense for violating them. Full information is found in the
course syllabus, which you should review before starting.
