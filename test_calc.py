from calc import *
import pytest


class TestClass:

    def test_split_expression(self):
        assert split_num_operators("11+22-33*44/55") == ["11", "+", "22", "-", "33", "*", "44", "/", "55"]

    def test_evaluate(self):
        assert main(s="1+2*3-4/5") == 6.2

    def test_bracket_priority(self):
        assert main(s = "(2*((1+3)/(3/3)))") == 8


if __name__ == "__main__":
    pytest.main(['./'])
