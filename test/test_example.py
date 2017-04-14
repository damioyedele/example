import unittest

from src.example import Example


class ExampleTest(unittest.TestCase):

  def test_adds_two_numbers(self):
    adder = Example()

    self.assertEqual(3, adder.add_numbers(1, 2))
