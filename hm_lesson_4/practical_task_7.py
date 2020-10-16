from itertools import count
from math import factorial


def fibo_gen():
    for i in count(1):
        yield factorial(i)


n = 0
for el in fibo_gen():
    if n < 5:
        print(el)
        n += 1
    else:
        break