from random import randint
from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_currency, amount):
        pass

class FXConverter(Converter):
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2

class GXConverter(Converter):
    def convert(self, from_currency, to_currency, amount):
        tx = randint(1, 4)
        print(f'{amount} {from_currency} = {amount * tx} {to_currency}')
        return amount * tx


class App:

    def __init__(self, converter : Converter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App(GXConverter())
    app.start()