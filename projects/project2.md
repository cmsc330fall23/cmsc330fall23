# Project 2
Due: September 19th, 2023 at 11:59 PM

The breakdown of tests is 30% public, 50% semipublic and 20% secret. As a reminder:

`publics`: You have the code we use for these tests, and you can run these tests locally or on gradescope.<br>
`semipublics`: You don't have the code for these tests, but you know if you are failing them on gradescope.<br>
`secrets`: You don't have the code, and you don't know if you're failing them until grades are released.<br>

## Restrictions
You may not import any additional modules or libraries. We have already imported `reduce` and `re` for you. Do not modify these imports or add any additional imports for this project.

## Overview
Your job is to act like a modified ribosome. 
A ribosome is in charge of building proteins by reading RNA sequences and then
constructing amino acid chains, depending on what the sequence looks 
like. It does this by reading sequences of letters called codons. 
Some codons command the ribosome to add an amino acid to the chain, while others may
command to start or stop building an amino acid chain. 
In this project, we will have arbitrarily long codons and we'll implement five commands discussed later.

## Codon Sequences
You will read in two files, one of which has mappings from names to codon sequences.
The example below shows the structure of the codon mapping file: <br>
**Example codon.txt:**
```text
  START: GGG
  Methionine: AUG
  Lucine: CUU, CUC, CUA, CUG
  Glutamine: CAA, CAG
  STOP: UAG, UAA
  SWAP: CCC
  DEL: UUU
  EXCHANGE: AGC
```
In reality, both START and Methionine are the same sequence, in this case, we
will have them separated. For this project, you can assume the sequences for each codon are unique to that codon and there won't be overlap.

You will need to read in this file and store this data in a data structure of
your choice, as it will be needed later.

## Building the Protein

Typically a sequence like `GGGCUACAACUGUAA` would build a protein consisting of
Lucine -> Glutamine -> Lucine (GGG -> CUA -> CAA -> CUG -> UAA). 
However, to make things interesting, it is possible for the sequence to have noise in it. 
The sequence `GGGCCUAACAACUGAUAA` would also build the same chain, because the 
codons found are (GGG -> C -> CUA -> A -> CAA -> CUG -> A -> UAA). This is 
because GGG is valid, but CCU is not valid so it moves on to CUA which is valid.  

Additionally, we have five commands with special effects:
```text
  START: Starts building an amino acid chain
  STOP: Stops building an amino acid chain
  DEL: Deletes an amino acid from the chain
  EXCHANGE: Exchanges the amino acid for another possible sequence
  SWAP: Swaps two amino acids in the chain
```

These commands will modify the chain. These 5 special commands will not operate on each other.
(For example, reading this chain with a prefix evaluation: "START DEL SWAP Methionine Lucine" 
DEL will NOT delete SWAP, therefore this chain will first swap Methionine with Lucine: 
"START DEL Lucine Methionine", then will delete Lucine, which produces just "Methionine")
Assuming reading left to right with a prefix evaluation, "GGGCUAUUUCAACUGUAA" (GGG CUA UUU CAA CUG UAA) 
will make a protein consisting of Lucine -> Lucine (CUA -> CUG) because DEL (UUU) will delete Glutamine (CAA) (based on the codon.txt file above).  

Other examples: 
```text
  GGG CUA AGC CAA CUG UAA -> CUA CAG CUG
  This will exchange CAA to CAG since Glutamine has two possible codons
  
  GGG CUA CCC CAA CUG UAA -> CUA CUG CAA
  This will swap the next two codons after the swap codon is seen 
```
To make this even more complicated, since mRNA can come from either side
of the DNA double helix, it is possible we are reading a sequence "backwards".

So, this chain "GGG CUA CAA CUG UAA" (reading left to right) is equivalent to this
chain "AAU GUC AAC AUC GGG" (reading right to left).
Additionally, consider this chain (reading right to left) "GGG AUC AAC GUC AAU"
which translates to "START <- Lucine <- Glutamine <- Lucine <- STOP" 
This chain reaches the start indicator too late to actually return 
anything from operating on it. 

Additionally, we have a variable operator position. 
Other examples: 
```text
  Assume we are reading left to right. 
  
  Sequence: Glutamine Methionine SWAP Lucine Valine
  
  If we use an Infix notation (1 + 2)
  The sequence becomes: Glutamine Lucine Methionine Valine
  
  If we use a Postfix notation (1 2 +)
  The sequence becomes: Methionine Glutamine Lucine Valine
  
  If we use a Prefix notation (+ 1 2)
  The sequence becomes: Glutamine Methionine Valine Lucine

  Using Prefix notation while reading right to left
  The sequence becomes: Methionine <- Glutamine <- Lucine <- Valine

  More examples of the Right to Left can be found further below.
```
For the DEL and EXCHANGE codons with an infix operator, apply these commands on the next amino acid (similar to pre-fix).
In order to keep track of this, you will need to read in a file that gives a name
to these evaluations: <br>
**Example eval.txt:**
```text
  Op1: L, PO
  Op2: R, I
  Op3: L, PR
  Op4: R, PO
```
+ **L** represents reading *Left to Right*
+ **R** represents reading *Right to Left*
+ **PO** represents *Post-Fix*
+ **PR** represents *Pre-Fix*
+ **I** represents *In-Fix*

## Functions to Implement
#### `read_codons(file)`
- **Description**: Given a path to a particular file, read all the contents of the file and store them in a data structure of your choice. Your data structure should be cleaned at the beginning of each read. As an added challenge, entries in the file can contain the regex pattern `\{\d+\}`. This pattern will have an effect on the entry. Consider the example `codons7.txt` file below:
```text
  Serine: A{4}GU
  SWAP: G{6}CA, GGGCCCAAA
  STOP: A{3}CU{1}AG
  Asparagine: UCA9GG
  Leucine: G{6}U{58}A
```
This means the sequence corresponding to the Serine amino acid is AAAAGU. Note the amino acid name left of the colon always starts with an uppercase letter and can be followed by any number of lowercase or uppercase letters. The colon touches the right side of the amino acid name and is followed by a space. The number of sequences for a single amino acid can range from 1 to infinity, and are always separated by a comma and a space. The valid sequence itself has at least 1 character of "A", "G", "U" or "C". Any other characters are invalid (For example the Asparagine line is invalid). Each codon will be on its own line in the file. The individual sequences must be all uppercase. If a line is invalid, it should be ignored.

- **Type**: `str -> None`
- **Examples**: 
```py
  read_codons(inputs/codon1.txt)
```

#### `read_evals(file)`
- **Description**: Given a path to a particular file, read all the contents of the file and store them in a data structure of your choice. Your data structure should be cleaned at the beginning of each read. Here is an example of an `eval.txt` file.
```text
  Order1: L, PO
  Order2: R, PR
  Order3: L, I
```
A valid order name consists of 1 or more alphanumeric characters (either upper or lowercase). The valid read order will be either an "L" or an "R". A valid operation order will be either "PO", "PR", or "I". If a line is invalid, ignore it. The colon touches the right side of the order name and is followed by a space. A comma and a space (in that order) separate the read order and the operation order. Each order will be on its own line in the file.
- **Type**: `str -> None`
- **Examples**: 
```py
  read_evals(inputs/orders1.txt)
```

#### `encode(sequence)`
- **Description**: Given a string of amino acid names separated by spaces, create the RNA sequence. If a codon does not exist, skip over it. Read left to right. If a particular amino acid has several sequences, take the longest one. If there are multiple longest sequences, return either (you only need to return one potential correct answer).
- **Type**: `str -> str`
- **Assumptions**: Assume your `read_codons` function was called.
- **Examples**:
```py
  encode("START Glutamine Lucine STOP") # could return "GGGCAAACUUUUAA"
  # Since amino acids have multiple possible RNA sequences, there are multiple correct answers
  encode("DEL Glutamine SWAP START") # could return "UUUCAGCCCGGG"
  encode("DEL INVALID Glutamine SWAP START") # could return "UUUCAGCCCGGG" and ignores the INVALID amino acid since it's not in the codon.txt
```

#### `decode(sequence)`
- **Description**: Given an RNA sequence, create a string of the amino acids separated by spaces. If there is noise, skip over it. Read left to right. Precedence is to take the longest sequence first.
- **Type**: `str -> str`
- **Assumptions**: Assume your `read_codons` function was called.
- **Examples**:
```py
  decode("GGGCAACUUUAA") # "START Glutamine Lucine STOP"
  decode("CUCCUUGGG") # "Lucine Lucine START"

  # There could be noise
  decode("CUCACUUAGGG") # "Lucine Lucine START"
  # CUC is Lucine
  # A,AC,ACU,ACUU,... are not valid so we skip to CUU which is lucine
  # A,AG,AGG,AGGG are not valid so we skip to GGG which is START 

  # Take the longest sequence
  # suppose START = GGG, STOP = UAC, DEL = GGGU, SWAP = AC
  decode("GGGUAC") -> "DEL SWAP"
  # Could be "GGG UAC" or "GGGU AC". Since len("GGGU") > len("GGG"), "GGGU" takes precedence
```

#### `operate(sequence, eval_name)`
- **Description**: Given a RNA sequence (with possible noise) and a name of an operation structure, return a RNA sequence having performed all operations on said sequence. If there is no STOP, read until the end of the sequence. If `eval_name` is not valid, return `None`. For DEL and EXCHANGE, if the operator is using infix notation, perform the operation on the next value. Reading the returned string left to right should follow the order in which you processed the string (see last example). Nothing should occur until START is reached. If there are multiple STARTs, continue building from the previous RNA sequence once you see another start (see the 3rd example down below). If an operator does not have the correct number of arguments, delete it before moving on to the rest of the sequence. Execute the inner most operator first.
- **Type**: `str -> str -> str or None`
- **Assumptions**: 
  - Assume your `read_codons` function was called.
  - Assume your `read_evals` function was called.
- **Examples**: For the examples below assume the codons and eval_names were read from the files labeled above as *codon.txt* and *eval.txt* 
```py
  operate("AUGGGGCUCUAACAG", "Op1") # "CUC"
  # The above translates to "Methionine START Lucine STOP Glutamine"
  # Since "Op1" says to read left to right, we skip Methionine since we haven't started yet, we start with START, build Lucine, STOP building, and skip over Glutamine.

  operate("GGGAUGCAGCUG","Op1") # "AUGCAGCUG"
  # The above translates to "START Methionine Glutamine Lucine"
  # Since there is no STOP we terminate at the end of the string

  operate("GGGAUGUAACAGGGGCUGUAG","Op1") # "AUGCUG"
  # The above translates to "START Methionine STOP Glutamine START Lucine STOP"
  # We do not add Glutamine since we STOP before, then we START again, add Lucine and then STOP

  operate("GAUAACGGGGUA","Op2") # "CAA"
  # Since "Op2" reads right to left, the above translates to "STOP <- Glutamine <- START <- Methionine"
  # So we skip over Methionine since we haven't started, then we start, add glutamine and then stop

  operate("GGGAUGUUUCUUGGG","Op1") # "CUU"
  # The above translates to "START Methionine DEL Lucine START"
  # Since "Op1" uses the Postfix operations, We START, add Methionine, DELete methionine, add Lucine, and ignore START since we already started

  operate("GAUUUCGGG","Op4") # "CUU"
  # Since "Op4" reads right to left, the above translates to "STOP <- Lucine <- START"
  # Since "Op4" uses the Postfix operations, We START, add Lucine, then STOP 

  operate("GGGAUGUUUCUUGGG","Op3") # "AUG"
  # The above translates to "START Methionine DEL Lucine START"
  # Since "Op3" uses the Prefix operations AND reads left to right, We START, add Methionine, DELete the next codon which is Lucine, then ignore START since we already started

  operate("GGGAGCCUU","Op3") # "CUC" or "CUA" or "CUG"
  # The above translates to "START EXCHANGE Lucine"
  # Since "Op3" is left to right and uses prefix operations, we START, then exchange the next code for an equivalent one for the same amino acid.
  # Since CUU is Lucine, we can exchange it for CUC, CUA, or CUG. Multiple right answers are allowed here.

  operate("GGGCCCCUUAUG","Op3") # "AUGCUU"
  # The above translates to "START SWAP Lucine Methionine"
  # Since "Op3" is left to right and prefix, we START, then swap the next two codons. So "Lucine Methionine" becomes "Methionine Lucine"

  operate("AAUUUUGACCCCUUCGUAGGG","Op4") # "CUUAUG"
  # Since "Op4" reads right to left, the above translates to "STOP <- DEL <- Glutamine <- SWAP <- Lucine <- Methionine <- START"
  # Because "Op4" uses post-fix operation, we START, then SWAP Lucine with Methionine, then DEL Glutamine, which results in "Methionine <- Lucine"
  # Then, we return in the order we read the sequence (right to left), thus returning: "Lucine Methionine" which is "CUUAUG".

  # When chaining operations together, operate on the inner operands first
  # this means "DEL SWAP Lucine Methionine" should first "SWAP" and then "Delete" assuming left to right and prefix notation. So the result should be "Lucine"
  # "DEL SWAP Lucine Methionine" -> "DEL Methionine Lucine" -> "Lucine"

  # If the operator is using infix notation, for unary operators DEL and EXCHANGE, perform the operation on the next value
  # If we are reading left to right using infix then "START Lucine DEL Methionine START" becomes "Lucine".
  # Whereas if we are reading right to left using infix then "START <- Lucine <- DEL <- Methionine <- START" becomes "Methionine"

  # "AACUUCUUUGUAGGG" if reading right to left you get: "Glutamine <- Lucine <- DEL <- Methionine <- START". Using a prefix notation (PR) you should
  # get back "Glutamine <- Methionine". Then, we return in the order we read the sequence (right to left), thus returning: "Methionine Glutamine" which
  # would actually be "AUGCAA".
  # When returning the RNA sequence, you should return in this order: "AUGCAA" and NOT "AACGUA"

  # If there is an incorrect number of arguments to an operator, delete it before moving on.
  # START Methionine SWAP STOP
  # This should just return "Methionine" if reading left to right using prefix notation.
```

## Testing & Submission
Submission is similar to other projects. `add`, `commit`, and `push` your changes to your GitHub classroom repo. Once changes are synced you can execute the `submit` command to send your work to gradescope. Testing your code locally can be done using the same pytest process from project 1.

From the root directory of Project 2: `python3 -m pytest`. This command indicates the number of tests you're failing and why. 
Feel free to modify the public.py file in order to debug. If you make too many modifications you can always restore to the default state by copying from the git repository. 
You can also create student tests in the folder `p2/test/student` by adding the files `__init__.py` and `test_student.py`
