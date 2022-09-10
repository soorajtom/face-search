
import argparse
from utils.encode_utils import encode_images_from_directory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Searches recursively in the directory for images and extracts face encodings.")

    parser.add_argument("-i", "--img-dir", type=str, help="Image directory for recursive search", dest="img_dir", required=True)
    parser.add_argument("-b", "--base-dir", type=str, help="Base directory for all images. Defaults to image directory.", dest="base_dir", required=False)
    parser.add_argument("-o", "--output-file", type=str, help="Output file", dest="out_file", required=True)
    parser.add_argument("-s", "--skip-file", type=str, help="Skip file", dest="skip_file", required=False)
    parser.add_argument("-p", "--processes", type=int, help="No of processes", dest="processes", default=1)
    parser.add_argument("-f", "--force", help="Overwrite output file", dest="force", action='store_true', default=False)
    parser.add_argument("-a", "--add-only", help="Add only images not encoded already", dest="add_only", action='store_true', default=False)
    # parser.add_argument("-v", "--verbose", dest="verbose", action='store_true', default=False)

    args = parser.parse_args()

    encode_images_from_directory(**vars(args))