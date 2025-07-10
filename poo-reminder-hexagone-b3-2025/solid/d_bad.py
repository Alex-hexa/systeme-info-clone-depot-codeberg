from random import randint

class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2

class GXConverter:
    def convert(self, from_currency, to_currency, amount):
        tx = randint(1, 4)
        print(f'{amount} {from_currency} = {amount * tx} {to_currency}')
        return amount * tx


class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()