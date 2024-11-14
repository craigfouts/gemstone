"""
Author: Craig Fouts
"""

import numpy as np

HSBLOCKS = np.array([[0, 0],
                     [1, 1]], dtype=np.int32)

VSBLOCKS = np.array([[0, 1],
                     [0, 1]], dtype=np.int32)

CHBLOCKS = np.array([[0, 1, 0],
                     [1, 0, 1],
                     [0, 1, 0]], dtype=np.int32)

GGBLOCKS = np.array([[0, 1, 0, 2, 2, 2],
                     [1, 1, 1, 2, 0, 2],
                     [0, 1, 0, 2, 2, 2],
                     [3, 0, 0, 4, 4, 4],
                     [3, 3, 0, 0, 4, 0],
                     [3, 3, 3, 0, 4, 0]], dtype=np.int32)
