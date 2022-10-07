import pytest
from calc import *


class TestClass:
    """
    class with test cases
    """

    def test_split_expression(self):
        """
        test if the split_num_operators function can split numbers and operators
        """
        assert split_num_operators("11+22-33*44/55") == ["11", "+", "22", "-", "33", "*", "44", "/", "55"]

    def test_evaluate(self):
        """
        test if the main function can work like eval() to evaluate the correct result
        """
        assert main(s="1+2*3-4/5") == 6.2

    def test_bracket_priority(self):
        """
        test if the brackets can give the expressions within higher operation priority
        """
        assert main(s = "(2*((1+3)/(3/3)))") == 8


if __name__ == "__main__":
    pytest.main(['./'])
