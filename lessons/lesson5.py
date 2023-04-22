# модули
# встроенные модули
import math

print(math.pi)

from math import e as числоЕ

print(числоЕ)

# собвственные модули
from lesson3 import Bank

import add.hero
from add import hero

obj = Bank('name', 1000, '123resdfewgrs')
print(obj)

# внешние модули
import colorama
print(colorama.Back.RED,colorama.Fore.BLUE)
print('привет')