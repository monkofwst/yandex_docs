# 1.
```python
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class PayForm(QWidget):
    def __init__(self):
        super(PayForm, self).__init__()
        uic.loadUi('pay.ui', self)
        self.payButton.clicked.connect(self.get_data)

    def get_data(self):
        card_num = self.cardData.text()
        print(card_num)


def get_card_number(self):
    card_num = self.cardData.text()
    card_num = ''.join(card_num.split())
    if card_num.isdigit() and len(card_num) == 16:
        return card_num
    else:
        return 404


def double(self, x):
    res = x * 2
    if res > 9:
        res = res - 9
    return res


def luhn_algorithm(self, card):
    odd = map(lambda x: self.double(int(x)), card[::2])
    even = map(int, card[1::2])
    return (sum(odd) + sum(even)) % 10 == 0


def process_data(self):
    number = self.get_card_number()
    if number == 404:
        self.errorLabel.setText(
            "Введите только 16 цифр. Допускаются пробелы")
    elif self.luhn_algorithm(number):
        self.errorLabel.setText(
            "Ваша карта обрабатывается...")
    else:
        self.errorLabel.setText(
            "Номер недействителен. Попробуйте снова.")        
        
        
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
```
# 2.
```python
try:
    a = int(input("Введите целое число: "))
    print(a + 10)
except ValueError:
    print("Неверное число")
```
# 3.
```python
try:
    a = int(input("Введите целое число: "))
    print(a + 10)
except ValueError as ve:
    print("Неверное число")
    print(ve)
    print(dir(ve))
```
# 4.
```python
def get_card_number(self):
    card_num = self.cardData.text()
    if not (card_num.isdigit() and len(card_num) == 16):
        raise ValueError("Неверный формат номера")
    return card_num


def double(self, x):
    res = x * 2
    if res > 9:
        res = res - 9
    return res


def luhn_algorithm(self, card):
    odd = map(lambda x: self.double(int(x)), card[::2])
    even = map(int, card[1::2])
    if (sum(odd) + sum(even)) % 10 == 0:
        return True
    else:
        raise ValueError("Недействительный номер карты")


def process_data(self):
    try:
        number = self.get_card_number()
        if self.luhn_algorithm(number):
            print("Ваша карта обрабатывается...")
    except ValueError as e:
        self.errorLabel.setText(f"Ошибка! {e}")
```
# 5.
```python
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class CardError(Exception):
    pass


class CardFormatError(CardError):
    pass


class CardLuhnError(CardError):
    pass


class PayForm(QWidget):
    def __init__(self):
        super(PayForm, self).__init__()
        uic.loadUi('pay.ui', self)
        self.hintLabel.setText(
            'Введите номер карты (16 цифр без пробелов):')
        self.payButton.clicked.connect(self.process_data)

    def get_card_number(self):
        card_num = self.cardData.text()
        if not (card_num.isdigit() and len(card_num) == 16):
            raise CardFormatError("Неверный формат номера")
        return card_num

    def double(self, x):
        res = x * 2
        if res > 9:
            res = res - 9
        return res

    def luhn_algorithm(self, card):
        odd = map(lambda x: self.double(int(x)), card[::2])
        even = map(int, card[1::2])
        if (sum(odd) + sum(even)) % 10 == 0:
            return True
        else:
            raise CardLuhnError("Недействительный номер карты")

    def process_data(self):
        try:
            number = self.get_card_number()
            if self.luhn_algorithm(number):
                print("Ваша карта обрабатывается...")
        except CardError as e:
            self.errorLabel.setText(f"Ошибка! {e}")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
```