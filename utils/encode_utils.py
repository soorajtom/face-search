import os
import json
import time
import sys
from multiprocessing import Pool
from utils.file_utils import get_images_in_dir_recursive, remove_prefix

def encode_image(f):
    import face_recognition
    img = face_recognition.load_image_file(f)
    img_vector = face_recognition.face_encodings(img, model="cnn")
    return (f, img_vector)

def encode_images(img_list, out_file, processes, faces, base_dir):
    skip_list = []
    start = time.time()
    with Pool(processes=processes) as pool:
        results = pool.map(encode_image, img_list)
    end = time.time()

    for (fname, fv) in results:
        sub_path = remove_prefix(fname, base_dir)
        if len(fv):
            for i in range(len(fv)):
                faces[sub_path+"_"+str(i)] = list(fv[i])
        else:
            skip_list.append(sub_path)
    
    with open(out_file, 'w') as fp:
        json.dump(faces, fp, indent=4)
    
    return skip_list

def encode_images_from_directory(img_dir, out_file, processes, base_dir=None, force=False, add_only=False, skip_file=None):
    if os.path.exists(out_file) and not force and not add_only:
        raise Exception("Output file already exists. Please remove the file or send -f option.")

    base_dir = base_dir if base_dir is not None else img_dir
    skip_list_set = set()
    if skip_file is None:
        skip_file = os.path.join(base_dir, ".skip_file")
    if os.path.exists(skip_file):
        with open(skip_file) as fp:
            skip_list_set = fp.readlines()
            skip_list_set = set([os.path.join(base_dir, l.strip()) for l in skip_list_set])

    image_paths = get_images_in_dir_recursive(img_dir, base_dir, skip_list_set)
    faces = dict()
    if add_only and os.path.exists(out_file):
        with open(out_file) as fp:
            faces = json.load(fp)
        existing_faces = set(map(lambda x: os.path.join(base_dir, "_".join(x.split("_")[:-1])),faces.keys()))
        image_paths = list(set(image_paths) - existing_faces)
    print("Collected %s images." % len(image_paths))

    start = time.time()
    new_skip_list = encode_images(image_paths, out_file, processes, faces, base_dir)
    end = time.time()

    with open(skip_file, "w") as fp:
        skip_list_set.update(new_skip_list)
        fp.writelines(["%s\n" % l.strip() for l in skip_list_set])
    print("Finished encoding images in %s seconds." % (end-start))
