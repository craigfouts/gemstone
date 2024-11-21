"""
Author: Craig Fouts
"""

import numpy as np
import os
import random

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

def make_bins(n_samples, n_bins, return_counts=False):
    """Apportions samples evenly into bins and returns the number of samples in
    each bin.
    
    Parameters
    ----------
    n_samples : int
        Number of samples.
    n_bins : int
        Number of bins.

    Returns
    -------
    list of shape=(n_bins,)
        Number of samples in each bin
    """

    counts = [n_samples//n_bins]

    for i in range(1, n_bins):
        counts.append((n_samples - sum(counts))//(n_bins - i))

    return counts
