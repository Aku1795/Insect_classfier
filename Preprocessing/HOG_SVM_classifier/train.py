from detector import ObjectDetector
import numpy as np
import argparse

ap = argparse.ArgumentParser()
# ap.add_argument("-a", "--annotations", required=True, help="path to saved annotations...")
# ap.add_argument("-i", "--images", required=True, help="path to saved image paths...")
# ap.add_argument("-d", "--detector", default=None, help="path to save the trained detector...")
args = vars(ap.parse_args())

print("[INFO] loading annotations and images")
annots = np.load("annotations.npy")
imagePaths = np.load("images.npy")

detector = ObjectDetector()
print("[INFO] creating & saving object detector")

detector.fit(imagePaths, annots, visualize=True, savePath="model.npy")
