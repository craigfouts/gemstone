"""
Author: Craig Fouts
"""

import numpy as np
from sklearn.datasets import make_classification
from .palettes import HSBLOCKS, VSBLOCKS, CHBLOCKS, GGBLOCKS
from .utilities import make_bins

def make_features(n_components, n_features, n_redundant=0, n_repeated=0, mean_scale=1., variance_scale=1.):
    n_informative = n_features - n_redundant - n_repeated
    means, _ = make_classification(n_components, n_features, n_informative, n_redundant, n_repeated, n_components, 1, scale=mean_scale)
    variances = variance_scale*np.random.rand(n_features)

    return means, variances

def make(blocks, n_features, n_equivocal=0, n_redundant=0, block_size=5, wiggle=0., shuffle=0., n_sets=1, plot=False):
    grid = np.repeat(np.repeat(blocks, block_size, 0), block_size, 1)
    _, counts = np.unique(grid, return_counts=True)
    n_shuffle = make_bins(int(shuffle*grid.size), counts.shape[0])
    

def show():
    pass
