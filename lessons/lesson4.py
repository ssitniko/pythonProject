# VENV виртуальное окружение
# модули в python: встроенные, внешние, собственные

import random

print(random.randint(1, 8))

from math import pi
from math import e as E
print(pi)
print(E)

from lesson3 import Bank

bank = Bank('Bank Account', 18, 1999)

import colorama
from art import tprint
print(colorama.Back.BLACK)
print(colorama.Fore.BLUE)
tprint('HELLO WORLD')
