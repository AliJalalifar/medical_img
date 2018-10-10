import numpy as np
import nrrd
import glob,os
from scipy.io import loadmat
header_path = './nrrds/'
header = nrrd.read_header(header_path+'3T1.nrrd')

print(header)


os.chdir('.\masks\\')
for file in glob.glob('*.mat'):
    labels = loadmat(file)['mask']
    labels = np.transpose(labels)
    print(labels)
    nrrd.write('./nrrd_masks/'+file[:-4]+ '.nrrd',labels,header)