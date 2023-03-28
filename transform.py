import cv2
import numpy as np
from PIL import Image

# python3 -m pip install opencv-python==4.6.0.66 --verbose
def open_image(filepath: str) -> np.ndarray:
    return cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2RGB)


def add_constant(image: np.ndarray, constant: int) -> np.ndarray:
    return cv2.add(image, constant)


def make_negative(image: np.ndarray) -> np.ndarray:
    return 255 - image


def multiply_by_constant(image: np.ndarray, constant: float) -> np.ndarray:
    image = image * constant
    return image.astype("uint8")


def power(image: np.ndarray, constant: float) -> np.ndarray:
    image = image.astype("float64")
    image /= np.max(image, axis=(0, 1)).astype("float64")
    image = image ** constant
    image *= 255
    return image.astype("uint8")


def logarithm(image: np.ndarray) -> np.ndarray:
    image = image.astype("float64")
    maximum = np.max(image, axis=(0, 1))
    image = 255 * np.log(1 + image) / np.log(1 + maximum)
    return image.astype("uint8")


def linear_contrast(image: np.ndarray) -> np.ndarray:
    minimum = np.min(image, axis=(0, 1))
    maximum = np.max(image, axis=(0, 1))
    image = (255 / (maximum - minimum)) * (image - minimum)
    return image.astype("uint8")


def local_otsu_thresholding(image: np.ndarray) -> np.ndarray:
    image = Image.fromarray(image).convert('L')
    return cv2.threshold(np.array(image), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def local_triangle_thresholding(image: np.ndarray) -> np.ndarray:
    image = Image.fromarray(image).convert('L')
    return cv2.threshold(np.array(image), 0, 255, cv2.THRESH_TRIANGLE)[1]


def mean_adaptive_thresholding(image: np.ndarray) -> np.ndarray:
    image = Image.fromarray(image).convert('L')
    return cv2.adaptiveThreshold(np.array(image), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1).astype("uint8")


def gaussian_adaptive_thresholding(image: np.ndarray) -> np.ndarray:
    image = Image.fromarray(image).convert('L')
    return cv2.adaptiveThreshold(np.array(image), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 1).astype("uint8")
