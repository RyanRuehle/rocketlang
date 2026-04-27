# RocketLang

RocketLang is a simple interpreted programming language that uses terms inspired by Rocket League.

RocketLang is line based. Each line contains one command. The first word is the command, and the rest of the line contains the arguments for that command.

RocketLang supports:

```txt
Variables
User input
Printing
String values
Integer multiplication
String concatenation
Repeated concatenation
String reversal
Equality comparison
Divisibility checking
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

RocketLang programs are written in `.txt` files.

Each line follows this basic format:

```txt
COMMAND value1 value2 result
```

The first word is the command. The values after it are arguments.

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
| `CHAT` | Prints a value | `CHAT "Hello World"` |
| `QUEUE` | Gets user input and stores it in a variable | `QUEUE name` |
| `BOOST` | Creates or updates a variable | `BOOST x 5` |
| `PINCH` | Multiplies two values and stores the result | `PINCH x y result` |
| `PASS` | Combines two values and stores the result | `PASS first second result` |
| `SPAM` | Repeatedly concatenates a value a chosen number of times | `SPAM char count result` |
| `FLIP` | Reverses a value and stores the result | `FLIP word result` |
| `RULE1` | Compares two values and stores true if they are equal | `RULE1 first second result` |
| `KICKOFF` | Checks if one integer is divisible by another integer | `KICKOFF number divisor result` |

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

Use `PINCH` to multiply two values.

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

Use `PASS` to combine two values.

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

## Repeated Concatenation

Use `SPAM` to repeatedly concatenate a value a chosen number of times.

Format:

```txt
SPAM value count result_variable
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

Another example:

```txt
BOOST word "ha"
BOOST count 3
SPAM word count result
CHAT result
```

Output:

```txt
hahaha
```

## Reversing A String

Use `FLIP` to reverse a value.

Format:

```txt
FLIP value result_variable
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

## Equality Comparison

Use `RULE1` to compare two values.

Format:

```txt
RULE1 first_value second_value result_variable
```

Example:

```txt
BOOST first "Rocket"
BOOST second "Rocket"
RULE1 first second result
CHAT result
```

Output:

```txt
true
```

Another example:

```txt
BOOST first "Rocket"
BOOST second "League"
RULE1 first second result
CHAT result
```

Output:

```txt
false
```

## Divisibility Checking

Use `KICKOFF` to check if one integer is divisible by another integer.

Format:

```txt
KICKOFF number divisor result_variable
```

Example:

```txt
BOOST number 15
BOOST divisor 3
KICKOFF number divisor result
CHAT result
```

Output:

```txt
true
```

Another example:

```txt
BOOST number 10
BOOST divisor 3
KICKOFF number divisor result
CHAT result
```

Output:

```txt
false
```

If the input is not a number, RocketLang prints a message and stores `false`.

Example:

```txt
BOOST number "k"
BOOST divisor 2
KICKOFF number divisor result
CHAT result
```

Output:

```txt
Input was not a number.
false
```

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
CHAT "Type something:"
QUEUE text
CHAT text
```

Run it:

```bash
py interpreter.py examples/cat.txt
```

Example input:

```txt
hello
```

Output:

```txt
hello
```

This works like a cat program because it copies user input directly to output.

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

This program uses the general `SPAM` command to repeatedly concatenate a value.

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
FLIP word reversed
RULE1 word reversed result
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

This program does not use a special palindrome command. It uses two broader commands:

```txt
FLIP reverses the word.
RULE1 compares the original word to the reversed word.
```

## is_even.txt

```txt
CHAT "Enter an integer:"
QUEUE number
BOOST divisor 2
KICKOFF number divisor result
CHAT result
```

Run it:

```bash
py interpreter.py examples/is_even.txt
```

Example input:

```txt
8
```

Output:

```txt
true
```

Another example input:

```txt
9
```

Output:

```txt
false
```

This program does not use a special even command. It uses the broader `KICKOFF` divisibility command. A number is even if it is divisible by 2.

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

Variables are stored in a Python dictionary.

Example:

```python
variables = {}
```

When the interpreter sees a variable name, it checks the dictionary and gets the stored value.

For example:

```txt
BOOST word "hello"
CHAT word
```

The interpreter stores `word` as `"hello"`, then prints it.

## Token Explanation

A token is one meaningful piece of a line.

Example:

```txt
KICKOFF number divisor result
```

The tokens are:

```txt
KICKOFF
number
divisor
result
```

The first token is the command. The remaining tokens are arguments.

RocketLang uses `shlex.split` because it keeps quoted text together.

Example:

```txt
CHAT "Hello World"
```

becomes:

```txt
CHAT
Hello World
```

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

The transpiler also generates helper functions in C.

`is_integer_string` checks whether a string is a valid integer.

`is_divisible` checks whether one integer is divisible by another integer.

Example generated C helper:

```c
int is_divisible(int number, int divisor) {
    if (divisor == 0) return 0;
    return number % divisor == 0;
}
```

## How RocketLang Commands Map To C

```txt
CHAT becomes printf.
QUEUE becomes scanf.
BOOST becomes strcpy.
PINCH becomes atoi, multiplication, and sprintf.
PASS becomes strcpy and strcat.
SPAM becomes a loop with strcat.
FLIP becomes a loop that copies a string backward.
RULE1 becomes strcmp.
KICKOFF becomes is_integer_string, atoi, and is_divisible.
```

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

Wrong:

```txt
KICKOFF number result
```

`KICKOFF` needs a number, a divisor, and a result variable.

Correct:

```txt
KICKOFF number divisor result
```

Wrong:

```txt
RULE1 word result
```

`RULE1` needs two values to compare and a result variable.

Correct:

```txt
RULE1 word reversed result
```

## What To Explain During The Demo

RocketLang is a simple line based interpreted language.

The interpreter reads each line, splits it into tokens, checks the command, and runs the matching Python code.

Variables are stored in a Python dictionary.

`RULE1` is a general equality comparison command. The palindrome program uses `FLIP` and `RULE1` together.

`KICKOFF` is a general divisibility command. The even program uses `KICKOFF number 2 result`.

The transpiler reads the same RocketLang syntax but writes equivalent C code instead of running the program directly.

The language has more than eight keywords and can run all seven required example programs.