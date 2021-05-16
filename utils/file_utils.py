import os

is_image = lambda x: x.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text 

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
