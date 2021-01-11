from nipy.labs.viz import plot_map, coord_transform
import nibabel as nib
import numpy as np
import os
import matplotlib.pyplot as plt

from run import DEBUG

# Set numpy to print only 2 decimal digits for neatness
np.set_printoptions(precision=2, suppress=True)


def create_png_activation_maps_from_niftii(path):

    dir_parent, file_name = os.path.split(path)
    path_nifti = path
    img_nifti = nib.load(path_nifti)
    sform = img_nifti.get_sform()
    data = img_nifti.get_fdata()
    plt.figure()
    plot_map(data, sform, cmap='gray', title="Activation Map")
    plt.show()

    pass


if __name__=="__main__":
    my_path, my_file_name = os.path.split(
        "tests/data/avg152T1_LR_nifti.nii.gz")
    create_png_activation_maps_from_niftii(my_path, my_file_name)
