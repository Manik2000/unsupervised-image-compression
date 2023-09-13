import numpy as np
from sklearn.cluster import MiniBatchKMeans


class ClusterCompressor:

    def __init__(self, img_array: np.ndarray, clusterer=MiniBatchKMeans):
        self.initial_image_array = img_array
        self.size = img_array.shape
        if clusterer == MiniBatchKMeans:
            self.clusterer = clusterer(batch_size=2048, n_init="auto")
        else:
            self.clusterer = clusterer()
        self.reshaped = None
        self.output_image_array = None

    def reashape(self):
        if len(self.size) == 3:
            self.reshaped = self.initial_image_array.reshape(self.size[0] * self.size[1], self.size[2])
        else:
            self.reshaped = self.initial_image_array.reshape(self.size[0] * self.size[1], 1)

    def compress(self, n_clusters: int=8) -> np.ndarray:
        self.clusterer.n_clusters = n_clusters
        if self.reshaped is None:
            self.reashape()
        self.clusterer.fit(self.reshaped)
        self.output_image_array = self.clusterer.cluster_centers_[self.clusterer.labels_]
        self.output_image_array = self.output_image_array.reshape(self.size)
        return np.array(self.output_image_array)
