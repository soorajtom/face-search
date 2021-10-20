import json

import face_recognition
from utils.encode_utils import encode_image_file
from utils.file_utils import get_config

config = get_config()

def get_recorded_faces(faces_json):
    if faces_json is None:
        faces_json = config['output_file']
    with open(faces_json) as fp:
        combined_vectors = json.load(fp)

    sample_labels = []
    sample_vectors = []
    for k,v in combined_vectors.items():
        sample_labels.append(k)
        sample_vectors.append(v)

    return sample_labels, sample_vectors

def search_one_face(labels, vectors, match_face, tolerance):
    if tolerance is None:
        tolerance = config['tolerance']
    similar_faces = []
    results = face_recognition.compare_faces(vectors, match_face, tolerance=tolerance)

    for i in range(len(results)):
        if results[i]:
            similar_faces.append(labels[i])
    return similar_faces

def search_one_face_from_file(f, tolerance=None, labelled_faces_json=None):
    _, face_encoding = encode_image_file(f)
    if len(face_encoding) == 0:
        return None
    labels, vectors = get_recorded_faces(labelled_faces_json)
    return search_one_face(labels, vectors, face_encoding[0], tolerance)
