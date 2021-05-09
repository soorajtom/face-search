import os
import json
import time
import sys
from multiprocessing import Pool

def encode_image(f):
    import face_recognition
    img = face_recognition.load_image_file(f)
    img_vector = face_recognition.face_encodings(img, model="cnn")
    return (f, img_vector)

def encode_images(img_list, out_file, processes):
    faces = dict()
    start = time.time()
    with Pool(processes=processes) as pool:
        results = pool.map(encode_image, img_list)
    end = time.time()

    for (fname, fv) in results:
        if len(fv):
            for i in range(len(fv)):
                faces[fname+"_"+str(i)] = list(fv[i])
    
    with open(out_file, 'w') as fp:
        json.dump(faces, fp, indent=4)