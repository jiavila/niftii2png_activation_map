docker build -t flywheel/niftii2png_activation_map:0.0.0_dev .
fw gear local --nifti tests/data/avg152T1_LR_nifti.nii.gz # nifti image
