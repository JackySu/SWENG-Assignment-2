from typing import List


operators = ['+', '-', '*', '/']

# the reason why left bracket has low priority is for when it is pushed into stack
# see !MARK 1!
priority = {'~': 0, '(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
# '~' works as an occupant simply does nothing
stack = ['~']
result = []


# split raw input into a list of nums and operators
def split_num_operators(a: str) -> List:
    res = []
    n = len(a)
    i = 0
    while i < n:
        if a[i].isdigit():
            if i >= n - 1:
                res.append(a[i])
                break
            else:
                for j in range(i + 1, n):
                    if not a[j].isdigit():
                        res.append(a[i:j])
                        i = j
                        break

        elif a[i] in operators or a[i] == '(' or a[i] == ')':
            res.append(a[i])
            i += 1

    return res


def operate(operator: str, a: str, b: str) -> None:
    a, b = float(a), float(b)
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b


def calculate() -> int:
    operand2, operand1 = result.pop(), result.pop()
    operator = stack.pop()
    ret = operate(operator, operand1, operand2)
    result.append(ret)
    return 0


def convert_to_postfix(expressions: List) -> None:
    for i in expressions:
        # add to result if it is a number
        if i.isdigit():
            result.append(i)

        elif i in operators:
            # !MARK 1!
            # pop from stack and calculate if it has lower priority
            while priority[stack[-1]] >= priority[i]:
                calculate()

            stack.append(i)
        # push into stack if it is the left bracket
        elif i == '(':
            stack.append(i)
        # if it is the right bracket then calculate until reaches the left bracket
        elif i == ')':
            while stack[-1] != '(':
                calculate()

            stack.pop()


def main():
    try:
        expression_list = split_num_operators(input("Enter expression: "))
        convert_to_postfix(expression_list)
        while (len(result) > 1):
            calculate()

        print(result[0])
    except IndexError:
        print("Error in expression, please re-input")


if __name__ == "__main__":
    while True:
        main()
