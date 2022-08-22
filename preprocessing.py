import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import tqdm

file_path = "a.jpg"
img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img.shape)

width = img.shape[1]
height = img.shape[0]
channels = img.shape[2]

img_arr = img.reshape([width * height, channels])

def X2image(X, width, height, channels = 3):
    # Converts an array X from sklearn to an RGB image.
    return X.reshape([height, width, channels])


print(img.shape, img_arr.shape)

