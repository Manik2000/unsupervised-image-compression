"""
Utility functions for image to array and array to image conversions.
"""
import numpy as np
from PIL import Image


def load_image_into_array(path: str) -> np.ndarray:
    """
    Load an image into a numpy array
    :param path: path to the image (str)
    :return: image array (numpy array)
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f'File {path} not found')
        return None
    except Exception as e:
        print(f'Error {e} while opening file {path}')
        return None
    return np.array(img)


def load_array_into_image(array: np.ndarray) -> Image:
    """
    Load an array into an image
    :param array: image array (numpy array)
    :return: image (PIL Image)
    """
    return Image.fromarray(array.astype('uint8'))
