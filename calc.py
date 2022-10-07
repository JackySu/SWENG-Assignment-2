from typing import List


# Shi Su updated on 30/9/2022
operators = ['+', '-', '*', '/']

# the reason why left bracket has low priority is for when it is pushed into stack
# see !MARK 1!
priority = {'~': 0, '(': 1, '+': 2, '-': 2, '*': 3, '/': 3}


# split raw input into a list of nums and operators
def split_num_operators(a: str) -> List:
    """_summary_

    Args:
        a (str): a string consists of numbers and operators

    Raises:
        Exception: illegal char if it is neither a number nor operator

    Returns:
        List: split input into a list of numbers and operators
    """
    a = a.strip().replace(" ", "")
    res = []
    n = len(a)
    i = 0
    while i < n:
        if a[i].isdigit():
            if i >= n - 1:
                res.append(a[i])
                break
            else:
                end = True
                for j in range(i + 1, n):
                    if not a[j].isdigit():
                        res.append(a[i:j])
                        end = False
                        i = j
                        break
                if end:
                    res.append(a[i:])
                    break  # reaches the end of expression

        elif a[i] in operators or a[i] == '(' or a[i] == ')':
            res.append(a[i])
            i += 1
        else:
            raise Exception(f"illegal char '{a[i]}' at index {i}")

    return res


def operate(operator: str, a: str, b: str) -> float:
    """_summary_

    Args:
        operator (str): operator symbol
        a (str): operand A
        b (str): operand B

    Raises:
        Exception: A / B when B is zero

    Returns:
        float: result of operation
    """
    a, b = float(a), float(b)
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        try:
            return a / b
        except ZeroDivisionError as exc:
            raise Exception("Can not be divided by 0") from exc


def calculate(result: List, stack: List) -> float:
    """_summary_

    Args:
        result (List): list to store number-only results
        stack (List): stack to store operators

    Returns:
        float: final result as float number
    """
    operand2, operand1 = result.pop(), result.pop()
    operator = stack.pop()
    ret = operate(operator, operand1, operand2)
    result.append(ret)
    return 0


def convert_to_postfix(expressions: List, result: List, stack: List) -> None:
    """_summary_

    Args:
        expressions (List): expressions of numbers and operators
        result (List): list to store number-only results
        stack (List): stack to store operators
    """
    for i in expressions:
        # add to result if it is a number
        if i.isdigit():
            result.append(i)

        elif i in operators:
            # !MARK 1!
            # pop from stack and calculate if it has lower priority
            while priority[stack[-1]] >= priority[i]:
                calculate(result, stack)

            stack.append(i)
        # push into stack if it is the left bracket
        elif i == '(':
            stack.append(i)
        # if it is the right bracket then calculate until reaches the left bracket
        elif i == ')':
            while stack[-1] != '(':
                calculate(result, stack)

            stack.pop()


def main(s=None) -> float:
    try:
        # '~' works as an occupant simply does nothing
        stack = ['~']
        result = []
        expression_list = split_num_operators(input("Enter expression: ")) if s is None else split_num_operators(s)
        convert_to_postfix(expression_list, result, stack)
        while (len(result) > 1):
            calculate(result, stack)
        return result[0]

    except IndexError:
        print("Error in expression, please re-input")
    except Exception as exc:
        print(exc)
    return None


if __name__ == "__main__":
    while True:

        res = main()
        if res is not None:
            print(res)
