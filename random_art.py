import random
from math import *

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    ret = []

    operation = ['+', '-', '*']

    operations = ['sin', 'cos', 'tan']

    var = ['(x)',
           '(y)',
           '(x+y)',
           '(x*y)',
           '(y*x + y**3)',
           '(x*y{}2*y)'.format(random.choice(operation)),
           '(x{a}x{b}x{c}y{d}y{e}y)'.format(a=random.choice(operation),
                                            b=random.choice(operation),
                                            c=random.choice(operation),
                                            d=random.choice(operation),
                                            e=random.choice(operation)),
           '(x{a}y{a}x)'.format(a=random.choice(operation))]

    for x in range(random.randint(1, 5)):
        ret.append(random.choice(operations) + random.choice(var))

    return lambda x, y: eval('{}'.format(random.choice(operation)).join(ret))


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
