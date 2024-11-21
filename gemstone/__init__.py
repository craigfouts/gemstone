"""
Author: Craig Fouts
"""

def __getattr__(attr):
    if attr == 'make':
        from ._core import make
        return make
    elif attr == 'show':
        from ._core import show
        return show
