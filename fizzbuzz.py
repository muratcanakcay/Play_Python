"""
Fİzzbuzz.

the ultimate question
"""


print('\n'.join(['Fizz'*(x % 3 == 2) + 'Buzz'*(x % 5 == 4)
                 or str(x + 1) for x in range(100)]))
