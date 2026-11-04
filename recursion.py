# this is type function where a function calling it itself

import sys
from time import sleep

print(sys.getrecursionlimit())
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())

def something(name):
    print('helo ',name)
    sleep(0.05)
    something('vamshi')

something('vamshi')