import numpy as np
import pandas as pd

from scipy.ndimage import gaussian_filter

__all__ = ['rand_array', 'smooth_image',"my_mat_solve","my_mean"]

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)


def rand_array(shape):
    return np.random.rand(*shape)

def my_mat_solve(A, b):
    return A.inv()*b

def my_mean(values):
    series = pd.Series(values)
    return series.mean()
