import sys
import shlex


variables = {}

def get_value(token):
    if token in variables:
        return variables[token]
    return token

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_even(number):
    
    #Check if a number is even without using the modulo operator.
    number = abs(number)

    while number > 1:
        number = number - 2

    return number == 0

def run_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        # Skip empty lines and comments
        if line == "" or line.startswith("#"):
            continue

        parts = shlex.split(line)
        command = parts[0].upper()

        try:
            if command == "CHAT":
                # Print the value of the given token (variable or literal)
                value = get_value(parts[1])
                print(value)

            elif command == "QUEUE":
                # Read input from user and store in variable
                name = parts[1]
                variables[name] = input()

            elif command == "BOOST":
                # Assign a value to a variable
                name = parts[1]
                value = get_value(parts[2])
                variables[name] = value

            elif command == "PINCH":
                # Multiply two numbers and store result in variable
                first = int(get_value(parts[1]))
                second = int(get_value(parts[2]))
                result_name = parts[3]
                variables[result_name] = str(first * second)

            elif command == "PASS":
                # Concatenate two strings and store result in variable
                first = get_value(parts[1])
                second = get_value(parts[2])
                result_name = parts[3]
                variables[result_name] = first + second

            elif command == "SPAM":
                # Repeat a character a given number of times and store in variable
                char = get_value(parts[1])
                count = int(get_value(parts[2]))
                result_name = parts[3]
                variables[result_name] = char * count

            elif command == "FLIP":
                # Reverse a string and store in variable
                word = get_value(parts[1])
                result_name = parts[2]
                variables[result_name] = word[::-1]

            elif command == "RULE1":
                # Check if a string is a palindrome and store "true" or "false" in variable
                word = get_value(parts[1])
                result_name = parts[2]

                reversed_word = word[::-1]

                if word == reversed_word:
                    variables[result_name] = "true"
                else:
                    variables[result_name] = "false"

            elif command == "KICKOFF":
                value = get_value(parts[1])
                result_name = parts[2]

                if is_integer(value):
                    number = int(value)

                    if is_even(number):
                        variables[result_name] = "true"
                    else:
                        variables[result_name] = "false"
                else:
                    print("Input was not a number.")
                    variables[result_name] = "false"

        except Exception as error:
            print(f"Error on line {line_number}: {error}")

# Main entry point: run the interpreter with the provided file
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py examples/helloworld.txt")
    else:
        run_file(sys.argv[1])