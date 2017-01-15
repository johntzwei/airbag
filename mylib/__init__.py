import __main__
import builtins
import sys
from .excepthook import CustomExcepthook

def pinkie(i,j,k):
    return 3

#force import of sys
builtins.sys = sys

#apply excepthook wrapper
__main__.__builtins__.sys.excepthook = CustomExcepthook
