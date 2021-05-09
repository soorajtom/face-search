import os
import argparse
from utils.encode_utils import encode_images

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--img-dir", type=str, help="Image location", dest="img_dir", required=True)
parser.add_argument("-o", "--output-file", type=str, help="Output file", dest="out_file", required=True)
parser.add_argument("-p", "--processes", type=int, help="No of processes", dest="processes", default=1)
parser.add_argument("-f", "--force", help="Overwrite output file", dest="force", action='store_true', default=False)

args = parser.parse_args()

if __name__ == "__main__":
    if os.path.exists(args.out_file) and not args.force:
        print("Output file already exists. Please remove the file or send -f option.")
    is_image = lambda x: x.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
    images = list(filter(is_image , os.listdir(args.img_dir)))
    print("Collected %s images." % len(images))
    image_paths = map(lambda x: os.path.join(args.img_dir, x), images)
    encode_images(image_paths, args.out_file, args.processes)