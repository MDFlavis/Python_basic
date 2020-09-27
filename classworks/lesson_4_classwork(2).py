from statistics import mean, median #import statistics as stat
import sys
import time
from itertools import cycle
import random
import functools
a = [itm for itm in range(2, 500) if itm & 1]

def statistics(x):
    return  0

def my_sum(x, y):
    return x + y

def my_pow(x, y):
    return x ** y

proc = {
    'sum': my_sum,
    'pow': my_pow
}

print(sys.argv)
if len(sys.argv) > 1:
    _, f, x, y, = sys.argv
    print(proc[f](float(x)), float(y))

tmp = ['one', 'two', 'three', 'four', 'five']



# for itm in cycle(range(10)):
#     print(itm)
#     time.sleep(0.5)
#     num = random.choice(tmp)
#     print(num)