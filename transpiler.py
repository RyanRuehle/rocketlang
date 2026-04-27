import sys
import shlex

# This function makes string values safe to place inside C quotes.
# For example, it escapes backslashes and quotation marks.
def c_string(value):
    return value.replace("\\", "\\\\").replace('"', '\\"')


# Main transpiler function.
# It takes a RocketLang file as input and creates a C file as output.
def transpile_file(input_file, output_file):
    # This set keeps track of every variable used in the RocketLang program.
    # Later, each variable becomes a char array in C.
    variables = set()

    # lines_out stores the final C code that will be written to the output file.
    lines_out = []

    # Read every line from the RocketLang program.
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Add the C library includes needed for printing, strings, and number conversion.
    lines_out.append("#include <stdio.h>")
    lines_out.append("#include <string.h>")
    lines_out.append("#include <stdlib.h>")
    lines_out.append("")

    # This helper function is added to the generated C code.
    # It checks if a number is even without using the modulo operator.
    lines_out.append("int is_even_without_modulo(int number) {")
    lines_out.append("    if (number < 0) number = -number;")
    lines_out.append("    while (number > 1) {")
    lines_out.append("        number = number - 2;")
    lines_out.append("    }")
    lines_out.append("    return number == 0;")
    lines_out.append("}")
    lines_out.append("")

    # Start the C main function.
    lines_out.append("int main() {")

    # temp is used for operations like reversing strings and checking palindromes.
    lines_out.append("    char temp[256];")

    # body_lines stores the C statements created from RocketLang commands.
    # Variable declarations are added before these statements later.
    body_lines = []

    # Go through the RocketLang program one line at a time.
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        # Ignore blank lines and comments.
        if line == "" or line.startswith("#"):
            continue

        # shlex.split separates the command and arguments.
        # It also keeps quoted strings together.
        # Example: CHAT "Hello World" becomes ["CHAT", "Hello World"]
        parts = shlex.split(line)

        # The first word is the RocketLang command.
        command = parts[0].upper()

        # CHAT prints either a literal value or a variable.
        # RocketLang: CHAT result
        # C: printf("%s\n", result);
        if command == "CHAT":
            value = parts[1]

            if value in variables:
                body_lines.append(f'    printf("%s\\n", {value});')
            else:
                body_lines.append(f'    printf("%s\\n", "{c_string(value)}");')

        # QUEUE takes user input and stores it in a variable.
        # RocketLang: QUEUE name
        # C: scanf("%255s", name);
        elif command == "QUEUE":
            name = parts[1]
            variables.add(name)

            body_lines.append(f'    scanf("%255s", {name});')

        # BOOST creates or updates a variable.
        # RocketLang: BOOST word "hello"
        # C: strcpy(word, "hello");
        elif command == "BOOST":
            name = parts[1]
            value = parts[2]
            variables.add(name)

            if value in variables:
                body_lines.append(f"    strcpy({name}, {value});")
            else:
                body_lines.append(f'    strcpy({name}, "{c_string(value)}");')

        # PINCH multiplies two values and stores the result.
        # Values are treated as strings in C, so atoi converts them to integers.
        # RocketLang: PINCH first second result
        # C: sprintf(result, "%d", atoi(first) * atoi(second));
        elif command == "PINCH":
            first = parts[1]
            second = parts[2]
            result = parts[3]
            variables.add(result)

            if first in variables:
                left = first
            else:
                left = f'"{c_string(first)}"'

            if second in variables:
                right = second
            else:
                right = f'"{c_string(second)}"'

            body_lines.append(f'    sprintf({result}, "%d", atoi({left}) * atoi({right}));')

        # PASS joins two strings together.
        # RocketLang: PASS first second result
        # C: strcpy(result, first);
        # C: strcat(result, second);
        elif command == "PASS":
            first = parts[1]
            second = parts[2]
            result = parts[3]
            variables.add(result)

            if first in variables:
                left = first
            else:
                left = f'"{c_string(first)}"'

            if second in variables:
                right = second
            else:
                right = f'"{c_string(second)}"'

            body_lines.append(f"    strcpy({result}, {left});")
            body_lines.append(f"    strcat({result}, {right});")

        # SPAM repeats a character or string a certain number of times.
        # RocketLang: SPAM char count result
        # C: uses a for loop and strcat.
        elif command == "SPAM":
            char = parts[1]
            count = parts[2]
            result = parts[3]
            variables.add(result)

            if char in variables:
                char_value = char
            else:
                char_value = f'"{c_string(char)}"'

            if count in variables:
                count_value = count
            else:
                count_value = f'"{c_string(count)}"'

            body_lines.append(f"    {result}[0] = '\\0';")
            body_lines.append(f"    for (int i = 0; i < atoi({count_value}); i++) {{")
            body_lines.append(f"        strcat({result}, {char_value});")
            body_lines.append("    }")

        # FLIP reverses a string.
        # RocketLang: FLIP word result
        # C: copies the word into temp, then copies it backward into result.
        elif command == "FLIP":
            word = parts[1]
            result = parts[2]
            variables.add(result)

            if word in variables:
                word_value = word
            else:
                word_value = f'"{c_string(word)}"'

            body_lines.append(f"    strcpy(temp, {word_value});")
            body_lines.append(f"    int len_{result} = strlen(temp);")
            body_lines.append(f"    for (int i = 0; i < len_{result}; i++) {{")
            body_lines.append(f"        {result}[i] = temp[len_{result} - i - 1];")
            body_lines.append("    }")
            body_lines.append(f"    {result}[len_{result}] = '\\0';")

        # RULE1 checks if a string is a palindrome.
        # A palindrome reads the same forward and backward.
        # RocketLang: RULE1 word result
        # C: compares characters from the front and back.
        elif command == "RULE1":
            word = parts[1]
            result = parts[2]
            variables.add(result)

            if word in variables:
                word_value = word
            else:
                word_value = f'"{c_string(word)}"'

            body_lines.append(f"    strcpy(temp, {word_value});")
            body_lines.append(f"    int len_{result} = strlen(temp);")
            body_lines.append(f"    int same_{result} = 1;")
            body_lines.append(f"    for (int i = 0; i < len_{result}; i++) {{")
            body_lines.append(f"        if (temp[i] != temp[len_{result} - i - 1]) same_{result} = 0;")
            body_lines.append("    }")
            body_lines.append(f'    if (same_{result}) strcpy({result}, "true");')
            body_lines.append(f'    else strcpy({result}, "false");')

        # KICKOFF checks if a number is even.
        # It calls the generated C helper function instead of using modulo.
        # RocketLang: KICKOFF number result
        # C: if even, stores "true", otherwise stores "false".
        elif command == "KICKOFF":
            number = parts[1]
            result = parts[2]
            variables.add(result)

            if number in variables:
                number_value = number
            else:
                number_value = f'"{c_string(number)}"'

            body_lines.append(f'    if (is_even_without_modulo(atoi({number_value}))) strcpy({result}, "true");')
            body_lines.append(f'    else strcpy({result}, "false");')

        # If the command is not recognized, print an error in the Python transpiler.
        else:
            print(f"Unknown command on line {line_number}: {command}")

    # Add C variable declarations near the top of main.
    # Every RocketLang variable becomes a 256 character array.
    for variable in sorted(variables):
        lines_out.append(f"    char {variable}[256];")

    # Add the translated C statements after the declarations.
    lines_out.extend(body_lines)

    # Finish the C main function.
    lines_out.append("    return 0;")
    lines_out.append("}")

    # Write the generated C code into the output file.
    with open(output_file, "w") as file:
        file.write("\n".join(lines_out))


# This lets the transpiler run from the command line.
# Example:
# py transpiler.py examples/helloworld.txt output/helloworld.c
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py transpiler.py examples/helloworld.txt output/helloworld.c")
    else:
        transpile_file(sys.argv[1], sys.argv[2])