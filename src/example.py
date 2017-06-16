class Calculator:
    def __init__(self):
        pass

    def add_numbers(self, n1, n2):
        return n1 + n2

    def subtract_numbers(self, x, y):
        return x - y

    def multiply_numbers(self, x, y):
        return x * y

class CoinChanger:
    def make_change(self, n1, n2):
        difference = n1 - n2
        answer = []
        while difference > 24:
            answer.append(25)
            difference = difference - 25
        while difference > 9:
            answer.append(10)
            difference = difference - 10
        if  difference > 4:
            answer.append(5)
            difference = difference - 5
        while difference > 0:
            answer.append(1)
            difference = difference - 1
        return answer

class Multiples:
    def divide(self, n1, n2):
        return n1 / n2

    def multiples_of_three_and_five_below(self, n):
        number = 1
        answers = []
        while number < n:
            if self.is_multiple_of_three(number) or self.is_multiple_of_five(number):
                answers.append(number)
            number = number + 1
        return answers

    def is_multiple_of_three(self, n):
        return n % 3 == 0

    def is_multiple_of_five(self, n):
        return n % 5 == 0

    def sum_multiples_of_three_and_five_below(self, n):
        return sum(self.multiples_of_three_and_five_below(n))
