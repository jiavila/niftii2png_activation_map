import flywheel
import logging
from pprint import pformat
import niftii2png_activation_map

DEBUG = True

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


        niftii2png_activation_map.create_png_activation_maps_from_niftii(
            path=path)





if __name__ == "__main__":
    main()
