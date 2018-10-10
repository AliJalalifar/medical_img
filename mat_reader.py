from scipy.io import loadmat
import numpy as np
mat = loadmat('./masks/3GTV2T1TumorMask.mat')
print(mat['mask'])