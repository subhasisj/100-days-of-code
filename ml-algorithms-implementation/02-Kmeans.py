from pickletools import optimize
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

class Kmeans(object):
    def __init__(self, k, max_iter=200, tol=1e-4):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, data):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
            
            #store centroids for comparision
            prev_centroids = dict(self.centroids)
        
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            # check if the centroids have changed
            optimized = True

            for centroid in self.centroids:
                prev_centroid = prev_centroids[centroid]
                current_centroid = self.centroids[centroid]
                if np.sum((current_centroid - prev_centroid) /prev_centroid)*100.0 > self.tol:
                    optimized = False

            if optimized:
                break
        

    def get_centroids(self):
        return self.centroids

    def predict(self,data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        return distances.index(min(distances))

if __name__ == "__main__":
    # Generate Random 2 dimensional dataset using make blobs
    X, y = make_blobs(n_samples=50, centers=4,cluster_std=0.60, random_state=0)

    # Initialize Kmeans
    kmeans = Kmeans(k=4)
    kmeans.fit(X)
 
    plt.scatter(X[:, 0], X[:, 1])
    # plot centroids
    centroids = kmeans.get_centroids()
    for centroids in centroids.values():
        plt.scatter(centroids[0], centroids[1],)
    plt.show()