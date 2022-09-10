import os
import yaml

is_image = lambda x: x.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def get_config(config_file="config.yaml"):
    with open(config_file) as fp:
        config = yaml.load(fp)
    return config

def key_to_filepath(key, image_dir):
    fname_pieces = key.split('_')
    fname_pieces = '_'.join(fname_pieces[:-1])
    return os.path.join(image_dir, fname_pieces)

def get_images_in_dir_recursive(img_dir, base_dir, skip_files=[]):
    img_files = []
    dir_contents = os.listdir(img_dir)
    for dir_elem in dir_contents:
        full_path = os.path.join(img_dir, dir_elem)
        if full_path in skip_files:
            continue
        if os.path.isdir(full_path):
            img_files.extend(get_images_in_dir_recursive(full_path, base_dir, skip_files))
        if os.path.isfile(full_path) and is_image(full_path):
            img_files.append(full_path)
    return img_files

def underscored_to_slash(key, base_dir):
    face_index = key.split('_')[-1]
    fname_pieces = key.split('_')[:-1]
    path = ""

    for i in range(len(fname_pieces)):
        part1 = '/'.join(fname_pieces[:i])
        part2 = '_'.join(fname_pieces[i:])
        local_path = '/'.join([part1, part2])
        path = os.path.join(base_dir, local_path)
        if os.path.exists(path):
            return False, "_".join([local_path, face_index])
    print(key, path)
    return True, ""


"""
from utils.file_utils import underscored_to_slash
import json
true = 0
false = 0
new_d = {}
with open("/home/melman/face-search/sample_combined.json") as fp:
    c = json.load(fp)
for f, v in c.items():
    x, sf = underscored_to_slash(f, "/media/melman/Legacy/0 G/OLD PHOTOS")
    if x:
        true += 1
    else:
        new_d[sf] = v
        false += 1

print (false, true)
with open("/home/melman/face-search/sample_combined_slash.json", "w") as fp:
    json.dump(new_d, fp)
"""