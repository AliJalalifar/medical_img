import nrrd

path = './masks/nrrd_masks/'
nrrd_file,header = nrrd.read(path+'3GTV2T1TumorMask.nrrd')

print(header)
print(nrrd_file)