import os
import sys
import glob
import dlib
import cv2

faces_folder = "multipie"

options = dlib.shape_predictor_training_options()

options.oversampling_amount = 300
# I'm also reducing the capacity of the model by explicitly increasing
# the regularization (making nu smaller) and by using trees with
# smaller depths.
options.nu = 0.05
options.tree_depth = 2
options.be_verbose = True

training_xml_path = os.path.join(faces_folder, "output/training_with_face_landmarks.xml")
print("Training file: {}".format(training_xml_path))
dlib.train_shape_predictor(training_xml_path, "./output/predictor.dat", options)

# Now that we have a model we can test it.  dlib.test_shape_predictor()
# measures the average distance between a face landmark output by the
# shape_predictor and where it should be according to the truth data.
print("\nTraining accuracy: {}".format(
    dlib.test_shape_predictor(training_xml_path, "predictor.dat")))