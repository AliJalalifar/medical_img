import nrrd
import matplotlib.pyplot as plt

patient_id = '11'
load_image_path = './nrrd_images/'
load_mask_path = './nrrd_images2/'
save_path = './png_images/'
# image,header = nrrd.read(load_image_path+patient_id+"T1.nrrd")
masks,header2= nrrd.read(load_mask_path,patient_id+'GTV2T1TumorMask.nrrd')
for i in range(0,len(masks)):
    plt.imsave(save_path + str(i)+'.png',masks[:,:,i],cmap="gray")
    # plt.imsave(save_path + str(i)+'_'+'.png',masks[:,:,i],cmap="gray")
    plt.show