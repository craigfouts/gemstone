"""
Author: Craig Fouts
"""

import numpy as np
import os
import random
from sklearn.datasets import make_classification

def set_seed(seed=9):
    """Sets a fixed environment-wide random state.
    
    Parameters
    ----------
    seed : int, default=9
        Random state seed.

    Returns
    -------
    None
    """

    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
        os.environ['PYTHONHASHSEED'] = str(seed)


