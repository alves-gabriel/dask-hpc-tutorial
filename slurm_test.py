# Shows the current environment
import os
print("\nCurrent conda environment:\n", os.environ['CONDA_DEFAULT_ENV'])

# Load necessary packages
import math
import numpy as np 
import scipy as scp
import matplotlib
import matplotlib.pyplot as plt
import sys

# Quspin
import quspin
print('\nquspin {} installed successfully and ready for use!\n'.format(quspin.__version__) )

L = 12
M = np.random.rand(2**L, 2**L)
eigvals, eigvecs = np.linalg.eig(M)
print(M)