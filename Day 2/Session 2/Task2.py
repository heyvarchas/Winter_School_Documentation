#Task: Write a program to execute K-means clustering for given image, used RGB coordinates.

import numpy as np                      # Import NumPy for numerical and array operations
import cv2                              # Import OpenCV for image processing and display

image = cv2.resize(
    cv2.imread(r"baboon_kmeans.jpeg"),
    (500, 500)
)
# Read the image from the given path and resize it to 500x500 pixels

clustered = np.zeros_like(image)
# Create an empty image array to store the clustered (output) image

k = 7
# Number of clusters for K-means

centroids = [
    image[np.random.randint(0, 500), np.random.randint(0, 500)]
    for _ in range(k)
]
# Randomly initialize k centroids by selecting random pixels from the image

print("Initial centroids:", centroids)  # Print the initial centroid RGB values

for iteration in range(3):              # Run the K-means algorithm for a maximum of 3 iterations
    clusters = [[] for _ in range(k)]
    # Create empty lists to store pixel indices for each cluster

    print("Iteration", iteration)       # Print current iteration number

    for i in range(500):                # Loop over image rows
        for j in range(500):            # Loop over image columns
            dists = [
                np.linalg.norm(c - image[i, j]) for c in centroids
            ]
            # Compute distance between the current pixel and each centroid (RGB space)

            kmin = np.argmin(dists)
            # Find the index of the closest centroid

            clusters[kmin].append((i, j))
            # Assign the pixel to the closest cluster

    old_centroids = centroids.copy()
    # Store old centroids to check for convergence

    for i in range(k):                  # Update each centroid
        if len(clusters[i]) > 0:
            rgb_cluster = np.array(
                [image[x, y] for x, y in clusters[i]]
            )
            # Collect RGB values of all pixels in the current cluster

            centroids[i] = np.mean(rgb_cluster, axis=0).astype(int)
            # Update centroid as the mean RGB value of the cluster

            print("Centroid", i, ":", centroids[i])
            # Print updated centroid value

    difference = np.abs(
        np.array(old_centroids) - np.array(centroids)
    )
    # Compute absolute difference between old and new centroids

    if (np.sum(difference) < 10):
        break                           # Stop if centroid change is very small (convergence)

for i in range(len(clusters)):          # Assign final cluster colors to the output image
    for x, y in clusters[i]:
        clustered[x, y] = centroids[i]
        # Set each pixel in the cluster to its centroid color

cv2.imshow("K-means result", clustered) # Display the clustered image
cv2.imshow("Actual Image", image)       # Display the original image
cv2.waitKey(0)                          # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()                 # Close all OpenCV windows