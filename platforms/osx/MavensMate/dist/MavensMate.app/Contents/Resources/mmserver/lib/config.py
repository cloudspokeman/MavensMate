import logging
import os.path
import sys

def __get_base_path():
    if hasattr(sys, 'frozen'):
        # print sys._MEIPASS
        # print sys.executable
        # print os.path.dirname(sys.executable)
        # config.base_path = os.path.dirname(sys.executable)
        return sys._MEIPASS
        #return os.path.dirname(os.path.dirname(__file__))
    else:
        return os.path.dirname(os.path.dirname(__file__))

def __get_is_frozen():
    if hasattr(sys, 'frozen'):
        return True
    else:
        return False

mm_path = None
frozen = __get_is_frozen()
base_path = __get_base_path()