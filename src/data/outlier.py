import numpy as np
from sklearn.pipeline import TransformerMixin
from scipy.spatial.distance import cdist


class OutlierExtractor(TransformerMixin):
    def __init__(self, columns, threshold=3, **kwargs):
        self.threshold = threshold
        self.columns = columns
        self.kwargs = kwargs

    def transform(self, X, y=None):
        X_ = np.asarray(X[self.columns])
        outliers_zscore = np.abs(cdist(self.avg[np.newaxis], X_) / self.std)[0]
        if y is not None:
            y = np.asarray(y)
            return (
                X[outliers_zscore <= self.threshold],
                y[outliers_zscore <= self.threshold]
            )
        return X[outliers_zscore <= self.threshold]
    
    def fit(self, X, y=None):
        X = np.asarray(X[self.columns])
        self.std = X.std()
        self.avg = X.mean(axis=0)
        return self