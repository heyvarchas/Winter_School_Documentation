#Task: Write a program to execute K-means clustering of the given set of points.

import numpy as np                      # Import NumPy for numerical and array operations
import matplotlib.pyplot as plt         # Import Matplotlib for plotting

points = np.array([
    [9, 7], [2, 3], [6, 15], [8, 7], [1, 3],
    [5, 14], [7, 9], [3, 2], [4, 15], [2, 2],
    [8, 9], [1, 1], [6, 14], [5, 15], [7, 7],
    [9, 8], [4, 14], [2, 4], [0, 2], [8, 10],
    [5, 16], [3, 3], [10, 8], [7, 8], [1, 2],
    [6, 16], [4, 16], [2, 1], [9, 9], [7, 15]
])
# Dataset containing 2D points for clustering

k = 3
# Number of clusters

centroids = points[np.random.choice(points.shape[0], k, replace=False)]
# Randomly initialize k centroids from the given points

for epoch in range(10):                # Run the K-means algorithm for a maximum of 10 iterations
    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
    # Compute the Euclidean distance from each point to each centroid

    labels = np.argmin(distances, axis=1)
    # Assign each point to the closest centroid (cluster index)

    new_centroids = np.array([
        points[labels == i].mean(axis=0) for i in range(k)
    ])
    # Compute new centroids by taking the mean of points in each cluster

    if np.allclose(centroids, new_centroids):
        break                           # Stop if centroids do not change significantly

    centroids = new_centroids           # Update centroids for the next iteration

print("Final centroids:\n", centroids)  # Print the final centroid coordinates
print("Cluster assignments:", labels)  # Print cluster index for each point

for i in range(k):                     # Plot each cluster separately
    cluster_points = points[labels == i]
    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        label=f'Cluster {i+1}'
    )

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker='X',
    s=200,
    c='black',
    label='Centroids'
)
# Plot centroids as large black X markers

plt.legend()                           # Show legend for clusters and centroids
plt.show()                             # Display the final clustering plot