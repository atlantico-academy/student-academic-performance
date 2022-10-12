import numpy as np
from sklearn.pipeline import TransformerMixin
from scipy.spatial.distance import cdist


class OutlierExtractor(TransformerMixin):
    def __init__(self, threshold=3, **kwargs):
        self.threshold = threshold
        self.kwargs = kwargs

    def transform(self, X, y=None):
        X = np.asarray(X)
        std = np.std(X)
        outliers_zscore = np.abs(cdist(X.mean(axis=0)[np.newaxis], X) / std)[0]
        if y:
            y = np.asarray(y)
            return (
                X[outliers_zscore >= self.threshold, :],
                y[outliers_zscore >= self.threshold, :]
            )
        return X[outliers_zscore >= self.threshold, :]
    
    def fit(self, *args, **kwargs):
        return self
