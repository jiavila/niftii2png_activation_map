from nipy.labs.viz import plot_map, coord_transform
import nibabel as nib
import numpy as np
import os
import matplotlib.pyplot as plt


# Set numpy to print only 2 decimal digits for neatness
np.set_printoptions(precision=2, suppress=True)

fig_rez_allowed = {'720p': (12.8, 7.2), '1080p': (19.2, 10.8)}

def create_png_activation_maps_from_niftii(
    path, path_out, fig_rez: str = None, cmap: str = None):

    if fig_rez is None:
        fig_rez = '720p'

    # Raise error if
    if fig_rez not in fig_rez_allowed:
        raise ValueError(
            f"fig_rez not one of {fig_rez_allowed.keys()}, got '{fig_rez}'"
        )

    if cmap is None:
        cmap = 'gray'

    dir_parent, file_name = os.path.split(path)
    path_nifti = path
    img_nifti = nib.load(path_nifti)
    sform = img_nifti.get_sform()
    data = img_nifti.get_fdata()

    # Create figure and plot
    fig = plt.figure(figsize=fig_rez_allowed.get(fig_rez), dpi=100)
    plot_map(data, sform, cmap=cmap, figure=fig)
    plt.savefig(path_out)
    # plt.show()





if __name__=="__main__":
    my_path = os.path.abspath(
        "tests/data/avg152T1_LR_nifti.nii.gz")
    create_png_activation_maps_from_niftii(my_path)
