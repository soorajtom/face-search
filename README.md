# face-search

## Design

### Input data
* Photos stored grouped by year, month, day.

### Output Data
- Path and thumbnail of similar faces.

### Steps
1. Input Data ingestion and face database creation.
    - This is performed the very first time the server created.
    - Extracts the face vector and stores it in the DB.
2. Create a service to compare an input face to similar faces in the database.
    - Django service that accepts the face (base64 or file).
    - compute the face vector from the input image.
    - find the most similar faces and return the paths.
3. Front End (Can be React or Django Templating) to upload the file.
    - Display the filepaths to the user + the thumbnail. 
4. Cron Job to search for new files to register into the database.


### TODO
1. Design the database schema
2. Design the face query algorithm


### Design Decisions

# Database Design

Schema:
1. VARCHAR name of file
2. VARCHAR path to the file
3. array of float for the face vector

