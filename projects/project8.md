# Project 8: Rust Spell Checker
## Due: Mon 11-Dec, 2023 at 11:59 pm
## Points: 100 public
- 40 unit/integration tests, 2pts per test
- 10 main/binary tests, 2pts per test

## FAQ: TBD (see pinned Piazza posts)

## Overview
This project builds a small spell checker which accepts strings and
uses a dictionary to mark words not in the dictionary or possibly
select an automatic correction for them.

Several techniques central to Rust are employed
- Basic file I/O is used to load a dictionary file, just vector of
  strings
- Regular expressions are used to traverse the string to be corrected
  and identify words that should be checked against the dictionary.
- A Rust [Trait](https://doc.rust-lang.org/book/ch10-02-traits.html)
  is used to describe the activity of correcting a word and several
  `struct`s are created that implement alternative versions of this
  behavior. 
- A [Generic
  Function](https://doc.rust-lang.org/book/ch10-01-syntax.html)
  is used to abstract the logic of traversing a string away from the
  specifics of how words should be corrected.

  
## Code Pack Files
The following files are distributed in the codepack.

| File                         | State    | Description                                    |
|------------------------------|----------|------------------------------------------------|
| `project8/`                  | Provided | Project root                                   |
| `Makefile`                   | Provided | Supplementary build file, try `make help`      |
| `Cargo.toml`                 | Provided | Options for the project                        |
| `README.md`                  | Provided | Project description                            |
| `.submit`                    | Provided | Allows submission to Gradescope through Github |
|                              |          |                                                |
| `src/p8_funcs.rs`            | EDIT     | Project functions to complete                  |
| `src/bin/spellcheck_main.rs` | EDIT     | Main Executable to complete                    |
|                              |          |                                                |
| `tests/test_p8funcs.rs`      | Testing  | Unit/Integration Tests for Functions           |
|                              |          | Try `make test-funcs`                          |
| `test_bin.sh`                | Testing  | Overview testing script for Binaries           |
|                              |          | Try `make test-bins`                           |
|                              |          |                                                |
| `test_all.org`               | Testing  | Point totaling for testing                     |
| `test_post_filter`           | Testing  | Used during points tallying                    |
| `test-data/*`                | Testing  | Test input files                               |
| `testy`                      | Testing  | Testing framework for totaling scores          |

## Build System
As before, you may use `cargo` commands directly such as `cargo build`
and `cargo test` but a `Makefile` is also provided to get some more
specificity. The `Makefile` will be used on Gradescope to total points
for the project. Below is a demonstration of building / testing via
the `Makefile`.

```sh
>> make clean
cargo clean

>> make
cargo build
   Compiling memchr v2.6.4
...
   Compiling project8 v0.1.0 (/home/kauffman/Dropbox/teaching/330-F2023/projects/p8-rust/project8)
    Finished dev [unoptimized + debuginfo] target(s) in 9.20s

>> make test-funcs
cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.03s
cargo test --test test_p8funcs
   Compiling project8 v0.1.0 (/home/kauffman/Dropbox/teaching/330-F2023/projects/p8-rust/project8)
    Finished test [unoptimized + debuginfo] target(s) in 1.44s
     Running tests/test_p8funcs.rs (target/debug/deps/test_p8funcs-8941f9cea10ad7b2)

running 40 tests
test test_ac_correct_word_show_sub_false1 ... ok
test test_ac_correct_word_show_sub_true1 ... ok
test test_ac_false_correct_string1 ... ok
...
test test_mark_corrected_load_string5 ... ok
test test_ac_false_correct_string3 ... ok
test test_ac_true_correct_string3 ... ok

test result: ok. 40 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 1.28s

>> make test-bin
./test_bin.sh

=============== SPELLCHECK_MAIN TESTS ===============
BUILDING PROGRAMS
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
PERFORMING SAMPLE RUNS
COMPARING EXPECTED (left) AND ACTUAL (right) OUTPUT
================ EXPECT ==================================         =================== ACTUAL ===============================
>> cargo -q run --bin spellcheck_main test-data/all-your-bass.t    >> cargo -q run --bin spellcheck_main test-data/all-your-bass.t
loading dictionary test-data/dict-bass.txt                         loading dictionary test-data/dict-bass.txt
opening file test-data/all-your-bass.txt                           opening file test-data/all-your-bass.txt
...
ok: Output matches, tests likely to pass
```

## Linux Tests
As before, Linux platforms support running the same points-based tests
as will be used on Gradescope via `make ltest`.
```sh
>> make help
Typical usage is:
  > make                          # build all programs
  > make test                     # run all tests
  > make test-funcs               # run tests for functions
  > make test-bin                 # run test for binaries
  > make clean-tests              # remove test-results/ directory
  > make clean                    # remove build files

LINUX ONLY (makes use of testy script which fails on MacOS
  > make ltest                    # run all tests and show scores, linux only
  > make ltest-funcs              # run function tests and show score, linux only
  > make ltest-bin                # run binary tests and show score, linux only
  > make ltest-funcs testnum=5    # run function tests test #5 only, linux only

>> make ltest
cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
cargo test --no-run			#build test programs
    Finished test [unoptimized + debuginfo] target(s) in 0.02s
  Executable unittests src/lib.rs (target/debug/deps/project8-1257d94cd0f8bd2a)
  Executable unittests src/bin/spellcheck_main.rs (target/debug/deps/spellcheck_main-b268913fa9657cc6)
  Executable tests/test_p8funcs.rs (target/debug/deps/test_p8funcs-06c9b4a40705deca)
./testy test_funcs.org 
============================================================
== test_funcs.org : P8 Functions
== Running 40 / 40 tests
1)  test_load_string_upper1              : ok
2)  test_load_string_upper2              : ok
3)  test_load_string_upper3              : ok
...
============================================================
RESULTS: 80 / 80 point earned

./testy test_bin.org 
============================================================
== test_bin.org : P8 Binary spellcheck_main
== Running 10 / 10 tests
1)  all-your-bass.txt dict-bass.txt mark           : ok
2)  all-your-bass.txt dict-bass.txt auto_show      : ok
...
============================================================
RESULTS: 20 / 20 point earned
```

## Ground Rules
As before, this is an individual assignment. You only receive help on
the project from staff members associated with the course.

Generally you may use functionality in Rust's standard library and the
external Regex crate which will be downloaded as part of the first
project build. No known functionality is forbidden for use but if
staff find certain functions that would make the project too easy,
additional restrictions may be announced before the deadline.

Guidance is given on techniques to use in each of the problems so keep
a copy of the README close.

# Functions in `src/p8_funcs.rs`
Most of the work will be in implementing functions in the
`p8_funcs.rs` file concluding with using these in
`spellcheck_main.rs`. This section offers guidance on each of the
elements that must be built.

## `load_string_upper()`
This function is primarily used to load "dictionary" files: files
filled with newline-separated words which are used as dictionaries.

Each string that is loaded should be converted to uppercase. This will
alleviate upper/lower case distinctions later when checking
spelling. Look through the Rust documentation on the `String struct`
to find an appropriate method to convert to upper case.

```rust
pub fn load_string_upper(fname: &str) -> Vec<String>
/// Allocate a vector and read all newline-separated strings from the
/// given `fname` into it returning it. As the strings are read in,
/// convert them to all upper case for ease of later use. This
/// function may panic!() if there are problems with the file. Words
/// should appera in the vector in the same order that they appeared
/// in the file.
///
/// EXAMPLES:
/// load_stringvec("test-data/small-dict.txt") -> ["APPLE","BANANA","CARROT"]
/// load_stringvec("test-data/google-10000-english.txt") -> ["THE", "OF", "AND", "TO", ...]
```

## `mark_corrected()`
This function implements the primary functionality sought after in a
spell checker. It scans a string for any words not in a given
dictionary (Vector of Strings) and marks them as in need of
correction. The essence of this is something like
```text
mark_corrected("this iz a mizsplled word",dictioary") 
            -> "this **iz** a **mizsplled** word"
```
where the resulting string has all words not in the dictionary marked
up. Some implementation details appear below the synopsis.

```rust
pub fn mark_corrected(text: &String, dict: &Vec<String>) -> String 
/// Iterate through the words in String `text` and construct a
/// corrected version of the string. Any word not contained in `dict`
/// is "marked" in the corrected version with double asterisks around
/// it.
/// 
/// WORDS / REGEXS: Words are defined as contiguous sequences of a-z
/// or A-Z or ' (single quote).  Using a regular expression to iterate
/// over words is likely helpful.  Portions of the original string in
/// between the corrected data should be copied into the corrected
/// version verbatim. Determining the starting / ending index of
/// matches is helpful for this.
///
/// CHECKING DICTIONARY: Words in `dict` are expected to be all upper
/// case so to check for the presence of a word in `dict`, it must
/// also be conveted to upper case, likely using a string method. Use
/// UPPERCASE versions of marked, incorrect words to make them easier
/// to see.
/// 
/// EXAMPLES:
/// let dict = vec!["APPLE","BANANA","ONION"];              // NOTE: types are slightly wrong, Sting vs str
/// mark_corrected("grape     apple  \n onion\n",&dict)     // string to correct
///             -> "**GRAPE**     apple  \n onion\n"        // corrected version
/// 
/// let dict = vec!["apple","banana","onion"];              
/// mark_corrected(" 12  3456 . ,,  78 0.123",&dict)        // string to correct
///             -> " 12  3456 . ,,  78 0.123"               // corrected version
/// 
/// let dict = vec!["ALL","BASE","ARE","YOUR","US"];        
/// mark_corrected("All your bass are belong 2 us!!",&dict) // string to correct
///             -> "All your **BASS* are **BELONG** 2 us!!" // corrected version
/// 
```

### Use of Regular Expressions
As the docstring outlines, Regular Expressions will make this task
easier. The `regex` package is set up as dependency of the project so
will be available with the correct `use` statements. Look back at
Project 7 if you need inspiration on this.

Note the notion of a "word" that is described in the docstring:
contiguous sequences of upper/lower case characters and the apostrophe
(single quote '). Set up a regular expression that matches these to
idenitfy words.

### Iterating with Regexs
A good way to use the regex engine is to iterate through the given
`text` in a loop looking for patterns that constitute a word. This
should (hopefully) be familiar from both prior Rust work from project
7 as well as previous work on regexs in other languages. 

### Building a Corrected String
To construct the new corrected string while iterating through the old
one, a reasonable approach is as follows.

1. Begin with an empty `corrected` string. Ensure it is mutable as it
   will grow.
1. Track the last position that the regex pattern matcher stopped int
   he string. Consult the documentation for
   [`Match`](https://docs.rs/regex/latest/regex/struct.Match.html)
   to find methods that give the start/end position of matches within
   the string being searched to help with this.
2. On finding a match (word), append onto `corrected` all characters
   from the last position to the start of the current match.
3. Next determine whether the current word is in the dictionary OR if
   it is not in the dictionary and needs to be marked. Append an
   appropriate version of the current matching word in (marked or not
   marked) into the `corrected` string.
4. Update the last position to the end of the current match and move
   to the next iteration.
5. At the end of the loop, it is likely ending characters will need to
   be copied in.
   
Below is a partially worked example of how this algorithm might
flow. Use this to help you understand how to build out the code for `mark_corrected()`.
```text
let dict = vec!["AT","I'M","COMFY"];
mark_corrected("  At  home:  I'm   comfy!",&dict)

          1         2
0123456789012345678901234 : index
  At  home:  I'm   comfy! : string

corrected = ""
lastpos = 0

match="At", beg=2, end=4
append 0 to 2 to corrected = "  "
"AT" IN dictionary
append "At" to corrected = "  At"
lastpos=4

match="Home", beg=6, end=10
append 4 to 6 to corrected = "  At  "
"home" NOT in dictionary
append "**HOME**" to corrected = "  At  **HOME**"
lastpos=10

match="I'm", beg=13, end=15
append 10 to 13 to corrected = "  At  **HOME**:  "
"I'm" IN dictionary
append "I'm" to corrected = "  At  **HOME**:  I'm"
lastpos=15
...
```   
   


## `trait Corrector` and the `correct_string()` Generic Function
Examine the Trait below.

```rust
/// Sets up a placeholde for implementing several correction schemes
pub trait Corrector {
  /// Produce a corrected version of the given word, possibly marked
  /// as needing attention or having a correction provided
  fn correct_word(&mut self, word: &str) -> String;
}
```

The following function uses a datum which implements this trait as
dictated by generic `<T>` parameter and  the constraint placed on its
type by the `where` clause.
```rust
pub fn correct_string<T>(text: &String,
                         dict: &Vec<String>,
                         corrector: &mut T)
                         -> String
where T: Corrector

/// Similar to `mark_corrected()` but uses a Corrector to produce the
/// corrected strings. Any word found while scanning `text` that is
/// does not have an upcased version in `dict` is passed to
/// `corrector.correct_word()` which will give produce a String to
/// replace it with in the corrected version. The general algorithm
/// and specific considerations are identical to `mark_corrected()`
/// 
/// EXAMPLES:
/// let dict = vec!["APPLE","BANANA","ONION"];              
/// let mut mc = MarkCorrector::new(">>","<<");             // use marking corrector
/// mark_corrected("grape     apple  \n onion\n",&dict,mc)  // string to correct
///             -> ">>GRAPE<<     apple  \n onion\n"        // corrected version
/// 
/// let dict = vec!["ALL","BASE","ARE","YOUR","US"];          
/// let mut ac = AutoCorrector::new(&dict,false);             // use auto corrector
/// mark_corrected("All your bass are belong 2 us!!",&dict,ac)// string to correct
///             -> "All your BASE are ALL 2 us!!"             // corrected version
/// 
```

There is no need to change anything about the `Corrector` trait. What
needs to be done is to implement the `correct_string()` function. Much
of the code from `mark_corrected()` can be transferred in.  All that
`correct_string()` does is to replace the specific "mark incorrect
words with **" by the specific functionality provided by
`corrector.correct_word(word)`.  There should be little code to
change here

**Pedagogical Note**: The functions `mark_corrected() /
correct_string()` are nearly identical and one could imagine ditching
`mark_corrected()` for the more general `correct_string()`.  However,
it is good for students to have a chance to work on the core logic of
the replacement algorithm and then worry about the generic version of
it. The project design reflects this.

## `MarkCorrector`
The intent of this struct is to abstract the "marking with **" idea
for marking words.  When created via `MarkCorrector::new(beg,end)`,
the begin/end strings are used around words which need
correction. This struct implements the `Corrector` trait so can then
be used int he generic algorithm `correct_word()` to mark words to
taste. Implement the "constructor" (`new()` function) for it then
implement the `correct_word()` function in an implementation block
tied to the `Corrector` trait.

```rust
/// This struct implements marking incorrect words with a begin/end
/// string pair so that they can identified and corrected later.
pub struct MarkCorrector {
  beg_mark: String,
  end_mark: String,
}

impl MarkCorrector {
  pub fn new(beg_mark: &str, end_mark: &str) -> MarkCorrector
  /// Create a MarkCorrector with the given begin/end markings
}

impl Corrector for MarkCorrector {
  fn correct_word(&mut self, word: &str) -> String
  /// Implementation of the correct_word() function to give
  /// MarkCorrector the Corrector trait. This function will return a
  /// given `word` with the begin/end marking strings prepended and
  /// appended and the word upcased. The format!() macro is useful for
  /// this.
  /// 
  /// EXAMPLES:
  /// let mut mc = MarkCorrector::new(">>","<<");
  /// mc.correct_word("incorrect") -> ">>INCORRECT<<"
  /// mc.correct_word("blergh") -> ">>BLERGH<<"
  /// 
  /// let mut mc = MarkCorrector::new("","!fixme");
  /// mc.correct_word("incorrect") -> "INCORRECT!fixme:"
  /// mc.correct_word("blergh") -> "BLERGH!fixme"
}
```


## `AutoCorrector`
The `AutoCorrector` structure also implements the `Corrector` trait so
can be used with `correct_word()`.  It takes a more aggressive
approach by providing a replacement word directly.  Historically such
auto-correction can have [humorous
outcomes](https://www.buzzfeednews.com/article/jessicamisener/the-30-most-hilarious-autocorrect-struggles-ever)
but are generally acknowledged to be very useful.

Below is an outline of the struct and its functions with details for
each function appearing in subsequent sections.

```rust
/// This struct is implements an automatic corrector that selects the
/// closest dictionary word to a given word. The show_sub field
/// controls whether automatic subsitions are shown with additional
/// information (true) or only the selected word (false).
pub struct AutoCorrector {
  dict_words: Vec<String>,
  show_sub: bool,
}

impl AutoCorrector {
  pub fn new(dict_words: &Vec<String>, show_sub: bool) -> AutoCorrector;
  pub fn closest_word(&self, word: &str) -> (String,usize);
}

impl Corrector for AutoCorrector {
  fn correct_word(&mut self, word: &str) -> String;
}
```
### `AutoCorrector::new(dict,show_sub)`
Creating an AutoCorrector requires 2 parameter. The use of the 2nd
`show_sub` parameter come up later so it only needs to be copied into
the appropriate field now.

To prevent difficult ownership issues, the `dict_words` vector should
be cloned as it is assigned to the appropriate field. This means that
the `AutoCorrector` owns all the data referred to in its fields. For
those interested in alternatives that avoid the larger memory
requirement of cloning, consider the last section on [Design
Limits](#design-limits) for future improvements to this system.

```rust
impl AutoCorrector {
  pub fn new(dict_words: &Vec<String>, show_sub: bool) -> AutoCorrector
  /// Create a new AutoCorrector with the given dictionary and
  /// show_sub value.  The dictionary is cloned during new() so that
  /// the AutoCorrector owns its own data. This simplifies ownership
  /// issues that would otherwise require lifetime annotations.
```

### `autocorrector.closest_word(query)`
The central functionality of an AutoCorrector is to look for the
"closest" word in its dictionary to given query.  "Closest"
necessitates some measure of distance between strings. A common metric
for this a form of Edit Distance called the [Levenshtein
Distance](https://en.wikipedia.org/wiki/Levenshtein_distance). It
denotes how many single character changes it takes to convert one
string to another. Changes include substituting a single character for
a different one, inserting a single character, or deleting one.
To compute this distance, Dynamic Programming is required which is
beyond the scope of this present project.  Thankfully, Rust has a
library "crate" called `edit_distance` which contains the handy
`edit_distance(a,b)` function to determine the distance between two
strings.

To gain access to the `edit_distance(a,b)` function, place a `use`
statement at the top of your source file. Typical `use` statements
look like
- `use crate_name;` to get use any function as with the namespace
  qualified as in: `crate_name::func_name(..)`
- `use crate_name::func_name;` to get use of one function without
  namespace qualification as in: `func_name(..)`
- `use crate_name::*;` to get use all functions from the crate without
  namespace qualification as in: `func_name(..)`
Pick one that is your preference for the `edit_distance` crate.

The essence of `closest_word(query)` is to iterate over all the words
in the AutoCorrector's `dict_words` and choose the one that has the
lowest `edit_distance()` to the query.  This is returned as a pair of
the best word and best distance. Note that some cloning may be needed
to assuage the borrow checker on returning strings.

```rust
impl AutoCorrector {

  pub fn closest_word(&self, word: &str) -> (String,usize)
  /// Iterates through the AutoCorrector's dict_words and finds finds
  /// the word with the lowest edit distance according to the
  /// edit_distance() function. The word passed in is upcased before
  /// calculating distances as the dictionary is expected to be all
  /// upcased words. If there are multiple strings that with the same
  /// edit distance to the given word, whichever one appears first in
  /// the dictionary is returned. Returns a pair of the
  /// (closest_word,distance). If dict_words is empty, this function
  /// returns a pair of ("",usize::MAX)
  ///
  /// EDIT DISTANCE: The edit_distance crate is listed as a dependency
  /// for this package and will be downloaded. It provides the
  /// edit_distance(a,b)->usize function which returns an unsigned
  /// integer measuring how many single character edits differentiate
  /// two strings passed in. This metrics is also referred to as the
  /// "Levenshtein distance" and requires the use of dynamic
  /// programming to calculate properly.
  /// 
  /// EXAMPLES: 
  /// let dict = vec!["ALL","BASE","ARE","YOUR","US"];          // should be String not &str
  /// let mut ac = AutoCorrector::new(&dict,false);             // use auto corrector
  /// ac.closest_word("bass")   -> ("BASE",1)
  /// ac.closest_word("belong") -> ("ALL",5)
  /// 
  /// let dict = vec!["A","B","C"];
  /// let mut ac = AutoCorrector::new(&dict,false);             
  /// ac.closest_word("a")   -> ("A",0)                         // in dictionary
  /// ac.closest_word("aa")  -> ("A",1)
  /// ac.closest_word("bbb") -> ("B",2)
  /// ac.closest_word("zz")  -> ("A",2)                         // alphabetic first
  /// 
  /// let dict = vec![];
  /// let mut ac = AutoCorrector::new(&dict,false);             // empty dictionary
  /// ac.closest_word("bass")   -> ("",18446744073709551615)
  /// ac.closest_word("belong") -> ("",18446744073709551615)
}
```

### `autocorrector.correct_word(query)`
AutoCorrectors return one of two types of strings from
`correct_word(query)` depending on their `show_sub` string.
- `show_sub: false` : return ONLY the closest word found the
  dictionary. This is what would be used in a user-level application. 
- `show_sub: true` : return a string showing the original query,
  closest word, and edit distance. This allows easier diagnosis of
  substitutions inline.
Look carefully at the formatting examples of the `show_sub: true`
cases below to ensure you produce the correct return string.

As before with `MarkCorrector`, the implementation of the
`correct_word()` function must be in an `impl` block tied to
`Corrector` to be compatible with the trait.

```rust
impl Corrector for AutoCorrector {
  fn correct_word(&mut self, word: &str) -> String;
  /// Implementation for Corrector. Uses closest_word() to find the
  /// closest dict_word to the given word. If the show_sub is true,
  /// returns a "verbose" correction that shows the original word,
  /// substituted word, and their edit distance in the format shown
  /// below. Otherwise, just returns the closest word found.
  ///
  /// EXAMPLES:
  /// let dict = vec!["ALL","BASE","ARE","YOUR","US"];
  ///
  /// let mut ac = AutoCorrector::new(&dict,false);       // show_sub is false
  /// ac.correct_word("bass") -> "BASE"                   // corrections are closest words    
  /// ac.correct_word("us") -> "US"
  /// ac.correct_word("belong") -> "ALL"
  // 
  /// let mut ac = AutoCorrector::new(&dict,true);        // show_sub is true
  /// ac.correct_word("bass") -> "(bass:BASE:1)"          // corrections include original
  /// ac.correct_word("us") -> "(us:US:0)"                // and closest word and edit
  /// ac.correct_word("belong") -> "(belong:ALL:5)"       // distance
```

## `spellcheck_main`
Fill in the template in the file
`project8/src/bin/spellcheck_main.rs`.  There are several `TODO` items
in the file which should be completed to finish a commandline
application that uses the functions in `p8_funcs.rs` to produce a
corrected version of a text file specified on the command line.
Sample uses are as follows.

```text
>> cargo -q run --bin spellcheck_main test-data/quotes.txt test-data/dict-google-10000.txt mark
loading dictionary test-data/dict-google-10000.txt
opening file test-data/quotes.txt
mode: mark

CORRECTED TEXT:
They could >>REFUDIATE<< what it is that this group is saying. They could
set the record straight.

They >>MISUNDERESTIMATED<< me.

That should be ">>POTATOE<<".

A Better >>AMERCIA<<.

Stress key ideas and >>VOCABLUARY<<.


>> cargo -q run --bin spellcheck_main test-data/quotes.txt test-data/dict-google-10000.txt auto
loading dictionary test-data/dict-google-10000.txt
opening file test-data/quotes.txt
mode: auto

CORRECTED TEXT:
They could REQUIRE what it is that this group is saying. They could
set the record straight.

They INVESTIGATED me.

That should be "POTATO".

A Better AMERICA.

Stress key ideas and VOCABULARY.


>> cargo -q run --bin spellcheck_main test-data/quotes.txt test-data/dict-google-10000.txt auto_show
loading dictionary test-data/dict-google-10000.txt
opening file test-data/quotes.txt
mode: auto_show

CORRECTED TEXT:
They could (refudiate:REQUIRE:4) what it is that this group is saying. They could
set the record straight.

They (misunderestimated:INVESTIGATED:7) me.

That should be "(potatoe:POTATO:1)".

A Better (Amercia:AMERICA:2).

Stress key ideas and (vocabluary:VOCABULARY:2).
```

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

# Design Limits
This section is optional reading and discusses some of the limitations
of the current design and how one might extend it.

## Dictionaries as Hash Tables
Dictionaries are good target to be Hash Table rather than a
Vector. This would enable faster lookup of presence / absence of words
in the dictionary. Rust has good data structures in its standard
library and converting over to use Hash Tables would make an easy
extension that improves computational efficiency .

## Dictionary Memory Usage
Dictionaries would ideally be comprised of a single large `String`
with words in a vector of `&str` slices of that string.  This would
allow an entire dictionary file to be read with slices taken for
each word. However, it is difficult to get this effect as Rust is
picky about the lifetimes of refs and the data that they refer
to. Seating up a struct with one field referring to another is known
to be difficult and might require use of Reference Counts or other
smart pointers. A more sophisticated version of dictionaries might
try to resolve this and enable something like
```rust
struct Dictionary {
  all_strings: String;  // owned by the dictionary
  words: Vec<&str>;     // refs into all_strings
}
```

## Generic Functions vs Dynamic Dispatch
While the generic function `correct_string()` is able to use any
`Corrector` implementation, one must still code specific cases for
any kind of corrector as in the following.
```rust
  match mode.as_str() {
  "mark" => {
    let mut mc = MarkCorrector::new(">>","<<");
    let corrected_text = correct_string(&file_text, &dict, &mut mc);
    println!("CORRECTED:\n{corrected_text}");
  },
  "auto" => {
    let mut ac = AutoCorrector::new(&dict,false);
    let corrected_text = correct_string(&file_text, &dict, &mut ac);
    println!("CORRECTED:\n{corrected_text}");
  }
  ...
```

The code layout allows the compiler to determine at compile time the
specific types used and "monomorphize" the generic function:
e.g. generate a specific version per type.

A common alternative that flows more nicely and avoids the repetitive
code is something like:
```rust
let mut corrector = 
match mode.as_str() {
  "mark" => MarkCorrector::new(">>","<<"),
  "auto" => AutoCorrector::new(&dict,false),
  ...
};
let corrected_text = correct_string(&file_text, &dict, &mut corrector);
println!("CORRECTED:\n{corrected_text}");
```
This patter is similar to what would be done in many OO langauges
such as Java where each specific item in the `match` implements a
common interface. Rust is capable of this pattern BUT it requires use
of Dynamic Dispatch. Rust requires use of some additional syntax and
types to enable Dynamic Dispatch. These are beyond the scope of the
present project but exploring Smart Pointers, `Box`, and the `dyn`
keyword are the path towards this.


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

