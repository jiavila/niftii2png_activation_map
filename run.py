import flywheel
import logging
from pprint import pformat
import niftii2png_activation_map
import os

DEBUG = False

# config debugger
logging.basicConfig()
log = logging.getLogger()
if DEBUG:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)


def main():

    with flywheel.GearContext() as gear_context:

        # ---------------------------------------------------------------------
        # Get file information and perform basic checks
        # ---------------------------------------------------------------------
        # Get the input file
        input_dict = gear_context.get_input("nifti")
        log.debug(f"Printing dictionary from input file:\n"
                  f"{pformat(input_dict)}")

        # Get file information
        # Get the base of the input file. This should be 'file'. Raise error
        # if it's not.
        base = input_dict.get("base")
        if not base:
            raise KeyError(f"Input file did not contain 'base' key.")
        if base != "file":
            raise TypeError(f"File base ('{base}') is not 'file'.")

        # Get the input file hierarchy
        hierarchy = input_dict.get("hierarchy")
        if not hierarchy:
            raise KeyError(f"Input file did not contain 'hierarchy' key.")

        # Get the file metadata
        metadata = input_dict.get('object')
        if not metadata:
            raise KeyError(f"Input file did not contain 'object' key.")

        # Get file location data
        location = input_dict.get("location")
        if not location:
            raise KeyError(f"Input file did not contain 'location' key.")

        # Get the path
        path = location.get("path")
        if not path:
            raise KeyError(f"Input file location did not contain 'path' key.")

        # Get the file name
        name = location.get("name")
        if not name:
            raise KeyError(f"Input file location did not contain 'name' key.")

        # ---------------------------------------------------------------------
        # Plot and save activation map based on user config options
        # ---------------------------------------------------------------------
        # Save the figure to the flywheel output as .png
        dir_out = "/flywheel/v0/output/"
        name_out = name.split('.')[0] + '.png'
        path_out = os.path.join(dir_out, name_out)
        niftii2png_activation_map.create_png_activation_maps_from_niftii(
            path=path,
            path_out=path_out,
            fig_rez=gear_context.config.get("fig_rez"),
            cmap=gear_context.config.get("cmap")
        )


if __name__ == "__main__":
    main()
