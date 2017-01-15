import __main__
import sys
import builtins

def pinkie(i,j,k):
    return 3

#force import of sys
builtins.sys = sys

#apply excepthook wrapper
__main__.__builtins__.sys.excepthook = pinkie
