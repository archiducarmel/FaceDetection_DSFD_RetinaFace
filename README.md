# Face detection using DSFD and RetinaFace!

This repo will simply and quickly help you to perform face detection


# Getting started

## Clone this repo

 - [ ] git clone *https://github.com/archiducarmel/FaceDetection_DSFD_RetinaFace.git* face_detection
 - [ ] cd *face_detection*

## Create a virtual environment

 - [ ] virtualenv *venv*
 - [ ] source *venv/bin/activate*
 - [ ] venv/bin/pip3 *install -r requirements*

## Create the *"weights"* folder and download weights

 - [ ] mkdir weights
 - [ ] cd weights
 - [ ] wget *https://github.com/archiducarmel/FaceDetection_DSFD_RetinaFace/releases/download/v0.1/RetinaFace_mobilenet025.pth*
 - [ ] wget *https://github.com/archiducarmel/FaceDetection_DSFD_RetinaFace/releases/download/v0.1/RetinaFace_ResNet50.pth*
 - [ ] wget *https://github.com/archiducarmel/FaceDetection_DSFD_RetinaFace/releases/download/v0.1/WIDERFace_DSFD_RES152.pth*

## Run the main script

 - [ ] Open *main.py* and modify paths if needed
 - [ ] cd ../
 - [ ] python3 *main.py*
