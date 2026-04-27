RocketLang is a simple programming language that uses terms from the video game Rocket League. 

# RocketLang

RocketLang is a simple interpreted programming language with Rocket League themed commands. It was created for the CMSC 4513 Programming Languages final project.

RocketLang supports:

```txt
Variables
User input
Printing
String values
Integer multiplication
String concatenation
String reversal
Palindrome checking
Even number checking
Repeating characters
```

## Project Files

```txt
interpreter.py
transpiler.py
README.md
examples/
    helloworld.txt
    cat.txt
    multiply.txt
    repeater.txt
    reverse_string.txt
    is_palindrome.txt
    is_even.txt
output/
```

## Language Features

RocketLang is line based. This means each line is one command.

Each command follows this basic format:

```txt
COMMAND value1 value2 result
```

The first word is the command. The values after it are the arguments for that command.

Example:

```txt
CHAT "Hello World"
```

## Basic Rules

```txt
1. Write one command per line.
2. Use quotes around text that has spaces.
3. Variable names cannot have spaces.
4. Blank lines are allowed.
5. Lines starting with # are comments.
6. Commands are not case sensitive, but uppercase is recommended.
```

Example comment:

```txt
# This is a comment
CHAT "Hello"
```

## Keywords

| Keyword | Meaning | Example |
| --- | --- | --- |
| CHAT | Prints a value | `CHAT "Hello World"` |
| QUEUE | Gets user input | `QUEUE name` |
| BOOST | Creates or updates a variable | `BOOST x 5` |
| PINCH | Multiplies two numbers | `PINCH x y result` |
| PASS | Combines two strings | `PASS first second result` |
| SPAM | Repeats a character or string | `SPAM char count result` |
| FLIP | Reverses a string | `FLIP word result` |
| RULE1 | Checks if a string is a palindrome | `RULE1 word result` |
| KICKOFF | Checks if an integer is even | `KICKOFF number result` |

## How To Run A RocketLang Program

Run this command from the project folder:

```bash
py interpreter.py examples/helloworld.txt
```

Example:

```bash
py interpreter.py examples/cat.txt
```

Programs that use input will pause and wait for the user to type something.

## How To Write Your Own RocketLang Program

A RocketLang program is just a `.txt` file.

Example file:

```txt
BOOST name "Ryan"
CHAT name
```

This stores `"Ryan"` in the variable `name`, then prints it.

Output:

```txt
Ryan
```

## Variables

Use `BOOST` to create or update a variable.

```txt
BOOST car "Octane"
CHAT car
```

Output:

```txt
Octane
```

Use `QUEUE` to get input from the user.

```txt
CHAT "Enter your name:"
QUEUE name
CHAT name
```

Example input:

```txt
Ryan
```

Output:

```txt
Ryan
```

## Printing

Use `CHAT` to print text or a variable.

```txt
CHAT "Hello World"
```

Output:

```txt
Hello World
```

You can also print a variable:

```txt
BOOST word "Rocket"
CHAT word
```

Output:

```txt
Rocket
```

## Multiplication

Use `PINCH` to multiply two numbers.

Format:

```txt
PINCH first_number second_number result_variable
```

Example:

```txt
BOOST first 3
BOOST second 4
PINCH first second answer
CHAT answer
```

Output:

```txt
12
```

## String Concatenation

Use `PASS` to combine two strings.

Format:

```txt
PASS first_string second_string result_variable
```

Example:

```txt
BOOST first "Rocket"
BOOST second "League"
PASS first second game
CHAT game
```

Output:

```txt
RocketLeague
```

## Repeating Characters

Use `SPAM` to repeat a character or string.

Format:

```txt
SPAM character count result_variable
```

Example:

```txt
BOOST char "*"
BOOST count 5
SPAM char count result
CHAT result
```

Output:

```txt
*****
```

## Reversing A String

Use `FLIP` to reverse a string.

Format:

```txt
FLIP word result_variable
```

Example:

```txt
BOOST word "hello"
FLIP word backwards
CHAT backwards
```

Output:

```txt
olleh
```

## Palindrome Checking

Use `RULE1` to check if a word is a palindrome.

A palindrome reads the same forward and backward.

Format:

```txt
RULE1 word result_variable
```

Example:

```txt
BOOST word "racecar"
RULE1 word result
CHAT result
```

Output:

```txt
true
```

Another example:

```txt
BOOST word "hello"
RULE1 word result
CHAT result
```

Output:

```txt
false
```

## Even Number Checking

Use `KICKOFF` to check if an integer is even.

Format:

```txt
KICKOFF number result_variable
```

Example:

```txt
BOOST number 8
KICKOFF number result
CHAT result
```

Output:

```txt
true
```

Another example:

```txt
BOOST number 9
KICKOFF number result
CHAT result
```

Output:

```txt
false
```

The even check does not use the modulo operator. It repeatedly subtracts 2 until the number is either 0 or 1.

## Required Example Programs

The `examples` folder contains the seven required programs.

## helloworld.txt

```txt
CHAT "Hello World"
```

Run it:

```bash
py interpreter.py examples/helloworld.txt
```

## cat.txt

```txt
BOOST first "Rocket"
BOOST second "League"
PASS first second result
CHAT result
```

Run it:

```bash
py interpreter.py examples/cat.txt
```

## multiply.txt

```txt
CHAT "Enter first single digit number:"
QUEUE first
CHAT "Enter second single digit number:"
QUEUE second
PINCH first second result
CHAT result
```

Run it:

```bash
py interpreter.py examples/multiply.txt
```

Example input:

```txt
3
4
```

Output:

```txt
12
```

## repeater.txt

```txt
CHAT "Enter a character:"
QUEUE char
CHAT "Enter how many times to repeat it:"
QUEUE count
SPAM char count result
CHAT result
```

Run it:

```bash
py interpreter.py examples/repeater.txt
```

Example input:

```txt
*
5
```

Output:

```txt
*****
```

## reverse_string.txt

```txt
CHAT "Enter a word:"
QUEUE word
FLIP word result
CHAT result
```

Run it:

```bash
py interpreter.py examples/reverse_string.txt
```

Example input:

```txt
hello
```

Output:

```txt
olleh
```

## is_palindrome.txt

```txt
CHAT "Enter a word:"
QUEUE word
RULE1 word result
CHAT result
```

Run it:

```bash
py interpreter.py examples/is_palindrome.txt
```

Example input:

```txt
racecar
```

Output:

```txt
true
```

## is_even.txt

```txt
CHAT "Enter an integer:"
QUEUE number
KICKOFF number result
CHAT result
```

Run it:

```bash
py interpreter.py examples/is_even.txt
```

Example input:

```txt
9
```

Output:

```txt
false
```

## Interpreter Explanation

The interpreter is written in Python.

The interpreter reads a RocketLang file one line at a time. It skips empty lines and comments. It uses `shlex.split` to separate each line into tokens while keeping quoted strings together.

Example:

```txt
CHAT "Hello World"
```

This becomes:

```txt
CHAT
Hello World
```

The first token is the command. The rest are arguments.

Variables are stored in a Python dictionary. When the interpreter sees a variable name, it checks the dictionary and gets the stored value.

For example:

```txt
BOOST word "hello"
CHAT word
```

The interpreter stores `word` as `"hello"`, then prints it.

## Transpiler Explanation

The transpiler is written in Python.

The transpiler reads a RocketLang file and creates matching C code. It uses the same command format as the interpreter, but instead of running the command, it writes C statements into an output `.c` file.

Example RocketLang:

```txt
CHAT "Hello World"
```

Generated C:

```c
printf("%s\n", "Hello World");
```

Example RocketLang:

```txt
QUEUE name
```

Generated C:

```c
scanf("%255s", name);
```

RocketLang variables become C character arrays.

Example:

```c
char name[256];
```

The transpiler also generates a C helper function called `is_even_without_modulo`. This checks if a number is even without using `%`.

## How To Transpile A RocketLang Program To C

Run this command from the project folder:

```bash
py transpiler.py examples/helloworld.txt output/helloworld.c
```

Example:

```bash
py transpiler.py examples/cat.txt output/cat.c
```

This creates a C file in the `output` folder.

## How To Compile Generated C Code

If `gcc` is installed, compile a generated C file with:

```bash
gcc output/helloworld.c -o output/helloworld
```

Then run it on Windows with:

```bash
output\helloworld.exe
```

## Demo Commands

Run the interpreter examples:

```bash
py interpreter.py examples/helloworld.txt
py interpreter.py examples/cat.txt
py interpreter.py examples/multiply.txt
py interpreter.py examples/repeater.txt
py interpreter.py examples/reverse_string.txt
py interpreter.py examples/is_palindrome.txt
py interpreter.py examples/is_even.txt
```

Run the transpiler examples:

```bash
py transpiler.py examples/helloworld.txt output/helloworld.c
py transpiler.py examples/cat.txt output/cat.c
py transpiler.py examples/multiply.txt output/multiply.c
py transpiler.py examples/repeater.txt output/repeater.c
py transpiler.py examples/reverse_string.txt output/reverse_string.c
py transpiler.py examples/is_palindrome.txt output/is_palindrome.c
py transpiler.py examples/is_even.txt output/is_even.c
```

## Common Mistakes

Wrong:

```txt
CHAT Hello World
```

This only prints `Hello` because the words are separated.

Correct:

```txt
CHAT "Hello World"
```

Wrong:

```txt
BOOST my name "Ryan"
```

Variable names cannot have spaces.

Correct:

```txt
BOOST my_name "Ryan"
```
