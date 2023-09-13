import numpy as np
from sklearn.decomposition import PCA


class PCACompressor:

    def __init__(self, image_array: np.ndarray):
        self.image_array = image_array
        self.size = image_array.shape
        self.pca = PCA()
        self.output_image_array = None

    @staticmethod
    def _compress_channel(pca: PCA, array: np.ndarray):
        pca.fit(array)
        n_dimensional = pca.transform(array)
        return pca.inverse_transform(n_dimensional)
    
    @staticmethod
    def _choose_n(n: int, size: tuple):
        if len(size) == 2:
            if n > min(size):
                n = min(size)
        else:
            a, b = size[0], size[1]
            if n > min(a, b):
                n = min(a, b)
        return n

    def compress(self, n_components: int=200) -> np.ndarray:
        self.pca.n_components = self._choose_n(n_components, self.size)
        if len(self.size) == 2:
            self.output_image_array = self._compress_channel(self.pca, self.image_array)
        else:
            colors = []
            for i in range(3):
                colors.append(self._compress_channel(self.pca, self.image_array[:, :, i]))
            self.output_image_array = np.dstack((colors[0], colors[1], colors[2]))
        return self.output_image_array
