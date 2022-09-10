from PIL import Image
import json
from multiprocessing import Pool
import os

def make_thumbnail(src, dest):
    if os.path.exists(dest):
        return
    img = Image.open(src)
    img.thumbnail((200,200))
    img.save(dest)

def handle(src_dir, dest_dir):
    with open("../studio_slash.json") as fp:
        c = json.load(fp)
    done = 0
    param_list = []
    for img in c.keys():
        fpath = "_".join(img.split("_")[:-1])
        dest_path = os.path.join(dest_dir, fpath.replace("/", "_"))
        src_path = os.path.join(src_dir, fpath)
        param_list.append((src_path, dest_path))
        # make_thumbnail(, dest_path)
        done += 1
        if done % 10000 == 0:
            print(done)
    with Pool(processes=4) as pool:
        pool.starmap(make_thumbnail, param_list)
