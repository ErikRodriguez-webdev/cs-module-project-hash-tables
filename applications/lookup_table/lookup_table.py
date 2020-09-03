import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


# set cache to empty dictionary
cache = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # check if x y tuple is in cache
    if (x, y) not in cache:
        # then calculate using x and y
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        # set x and y as dictionary key in cache with v as dictionary value
        cache[(x, y)] = v

    # once we go in above condition or get past above condition then retrieve value with x y tuple key
    return cache[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
