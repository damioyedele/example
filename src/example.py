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
