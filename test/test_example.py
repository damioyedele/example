import unittest

from src.example import Calculator, CoinChanger


class CalculatorTest(unittest.TestCase):

    def test_adds_two_numbers(self):
        adder = Calculator()
        self.assertEqual(3, adder.add_numbers(1, 2))

    def test_adds_two_different_numbers(self):
        calculator = Calculator()
        self.assertEqual(4, calculator.add_numbers(2, 2))

    def test_subtracts_two_numbers(self):
        subtracter = Calculator()
        self.assertEqual(5, subtracter.subtract_numbers(7, 2))

    def test_multiplies_numbers(self):
        calculator = Calculator()
        self.assertEqual(25, calculator.multiply_numbers(5, 5))

    def test_multiplies_other_numbers(self):
        calculator = Calculator()
        self.assertEqual(24, calculator.multiply_numbers(6, 4))

class CoinChangerTest(unittest.TestCase):

    def test_provides_a_penny(self):
        coin_changer = CoinChanger()
        self.assertEqual([1], coin_changer.make_change(100, 99))

    def test_provides_pennies(self):
        coin_changer = CoinChanger()
        self.assertEqual([1, 1, 1], coin_changer.make_change(100, 97))

    def test_provides_more_pennies(self):
        coin_changer = CoinChanger()
        self.assertEqual([5, 1, 1, 1], coin_changer.make_change(100, 92))

    def test_provides_dime(self):
        coin_changer = CoinChanger()
        self.assertEqual([10], coin_changer.make_change(100, 90))

    def test_provides_two_dimes(self):
        coin_changer = CoinChanger()
        self.assertEqual([10, 10], coin_changer.make_change(100, 80))

    def test_provides_a_quarter(self):
        coin_changer = CoinChanger()
        self.assertEqual([25], coin_changer.make_change(100, 75))

    def test_does_complex_stuff(self):
        coin_changer = CoinChanger()
        self.assertEqual([25, 25, 10, 5, 1, 1], coin_changer.make_change(100, 33))
