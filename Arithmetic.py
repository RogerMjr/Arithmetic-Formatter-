def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for index, value in enumerate(problems):

        operation = value.split(" ")

        if operation[1] not in "+-":
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            number1 = int(operation[0])
            number2 = int(operation[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        longest_val = max(len(operation[0]), len(operation[2]))
        width = longest_val + 2

        X1 = f"{operation[0]:>{width}}"
        X2 = operation[1] + f"{operation[2]:> {width - 1}}"
        d = "-" * width

        try:
            arranged_problems[0] += (' ' * 4) + X1
        except IndexError:
            arranged_problems.append(X1)

        try:
            arranged_problems[1] += (' ' * 4) + X2
        except IndexError:
            arranged_problems.append(X2)

        if args:
            ans = int(operation[0]) + int(operation[2]) if operation[1] == '+' else int(operation[0]) - int(
                operation[2])
            a = f"{str(ans):>(width)}"
        try:
            arranged_problems[3] += (' ' * 4) + a
        except IndexError:
            arranged_problems.append(a)

    output = f"{arranged_problems[0]}\n {arranged_problems[1]}\n {arranged_problems[2]}"
    output = output + f"\n{arranged_problems[3]}"

    if args else output

    return output