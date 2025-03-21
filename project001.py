"""Build an Arithmetic Formatter Project
"""
def arithmetic_arranger(problems, show_answers=False):
# Check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    result_line = []

    # Process each problem
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        # Check operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        # Check operand length
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width needed for formatting
        width = max(len(first), len(second)) + 2

        # Build each part of the arranged problem
        first_line.append(first.rjust(width))
        second_line.append(operator + " " + second.rjust(width - 2))
        dash_line.append("-" * width)

        # Compute the result for the problem
        if operator == '+':
            answer = str(int(first) + int(second))
        else:  # operator is '-'
            answer = str(int(first) - int(second))
        result_line.append(answer.rjust(width))

    # Join the individual components with four spaces between them
    arranged_first = "    ".join(first_line)
    arranged_second = "    ".join(second_line)
    arranged_dash = "    ".join(dash_line)

    # Prepare the final arranged string based on whether answers are to be displayed
    if show_answers:
        arranged_result = "    ".join(result_line)
        arranged_problems = arranged_first + "\n" + arranged_second + "\n" + arranged_dash + "\n" + arranged_result
    else:
        arranged_problems = arranged_first + "\n" + arranged_second + "\n" + arranged_dash

    return arranged_problems
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')