import numpy as np
import cv2
import argparse
from imutils.paths import list_images
from selectors.box_selector import BoxSelector

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to images dataset...")
# ap.add_argument("-a", "--annotations", required=True, help="path to save annotations...")
# ap.add_argument("-i", "--images", required=True, help="path to save images")
args = vars(ap.parse_args())

# annotations and image paths
# annotations = []
# imPaths = []

print(args["dataset"])

# loop through each image and collect annotations
for imagePath in list_images(args["dataset"]):
    print(imagePath)
    # load image and create a BoxSelector instance
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (400, 400))
    bs = BoxSelector(image, "Image")
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # order the points suitable for the Object detector
    pt1, pt2 = bs.roiPts
    (x, y, xb, yb) = [pt1[0], pt1[1], pt2[0], pt2[1]]
    print(x, y, xb, yb)


    # annotations.append([int(x), int(y), int(xb), int(yb)])
    # imPaths.append(imagePath)

# save annotations and image paths to disk
# annotations = np.array(annotations)
# imPaths = np.array(imPaths, dtype="unicode")
# np.save("annotations.npy", annotations)
# np.save("images.npy", imPaths)
