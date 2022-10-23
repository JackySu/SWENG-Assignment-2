from typing import List
import re
import math


# Shi Su updated on 30/9/2022
operators = ['+', '-', '*', '/', '^']

builtin_func = ['exp', 'log']
operators.extend(builtin_func)
# the reason why left bracket has low priority is for when it is pushed into stack
# see !MARK 1!
priority = {'~': 0, '(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4, 'exp': 4, 'log': 4}


def is_num(a: str) -> bool:
    return re.match(r"(?=.)([+-]?([0-9]+)(\.([0-9]+))?)([eE][+-]?\d+)?", a) is not None


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
    if len(a) == 0:
        return []

    res = []
    if a[0] == '-' or a[0] == '+':
        res.append('0')

    for match in re.finditer(r"[+\-*\^\/\(\)]|[0-9.]+|(exp)|(log)", a):
        if match:
            item = match.group(0)
            if not is_num(item) and item != '(' and item != ')' and item not in operators:
                raise Exception(f"illegal symbol {item}")
            res.append(item)

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
    b = float(b)
    if operator == 'exp':
        return math.exp(b)
    if operator == 'log':
        return math.log10(b)

    a = float(a)
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
    if operator == '^':
        return a ** b


def calculate(result: List, stack: List) -> float:
    """_summary_

    Args:
        result (List): list to store number-only results
        stack (List): stack to store operators

    Returns:
        float: final result as float number
    """

    operator = stack.pop()

    operand2 = result.pop()
    operand1 = result.pop() if operator not in builtin_func else ""

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
        if is_num(i):
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
        while (len(result) > 1 or len(stack) > 1):
            calculate(result, stack)
        return result[0]

    except IndexError as exc:
        print(exc)
        raise Exception(f'{exc}, maybe number of operators does not match operands') from exc
    except Exception as exc:
        print(exc)
        raise exc


if __name__ == "__main__":
    while True:
        try:
            res = main()
            if res is not None:
                print(f"Result: {float(res):.3f}")
        except Exception as e:
            print(e)
