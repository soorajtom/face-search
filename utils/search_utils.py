import json

import face_recognition
from utils.encode_utils import encode_image_file
from utils.file_utils import get_config

def get_recorded_faces(combined_vectors):
    # with open(faces_json) as fp:
    #     combined_vectors = json.load(fp)

    sample_labels = []
    sample_vectors = []
    for k,v in combined_vectors.items():
        sample_labels.append(k)
        sample_vectors.append(v)

    return sample_labels, sample_vectors

def search_one_face(labels, vectors, match_face, tolerance):
    similar_faces = []
    results = face_recognition.compare_faces(vectors, match_face, tolerance=tolerance)

    for i in range(len(results)):
        if results[i]:
            label = labels[i]
            if label[0] == "/":
                label = label[1:]
            similar_faces.append(label)
    return similar_faces

def search_one_face_from_file(f, tolerance, labelled_faces_json):
    _, face_encoding = encode_image_file(f)
    if len(face_encoding) == 0:
        return None
    labels, vectors = get_recorded_faces(labelled_faces_json)
    return search_one_face(labels, vectors, face_encoding[0], tolerance)
