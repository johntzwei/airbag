import traceback
import IPython as ip

def CustomExcepthook(type, value, tb):
    #TODO print out search queries, stackoverflow etc.
    #resources()

    #define all ipython stack navigation functions
    ip.embed()
