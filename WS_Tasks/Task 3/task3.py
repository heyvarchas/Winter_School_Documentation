import numpy as np
import cv2

# Load Images
img = cv2.imread("img.jpg")
bg_original = cv2.imread("bg.jpg")

if img is None or bg_original is None:
    print("Error: Could not find image files.")
    exit()

# Get original dimensions
h, w, _ = img.shape

# Resize background to match the original image size EXACTLY
bg = cv2.resize(bg_original, (w, h))

# Prepare Data (Flattening for K-means)
pixels = img.reshape((-1, 3)).astype(np.float32)

k = 5  # Higher K helps isolate the "edge" colors from the subject (But we can set the value based on our requirements)
iterations = 10
centroids = pixels[np.random.choice(pixels.shape[0], k, replace=False)]

print(f"Processing image of size {w}x{h}...")

# Optimized K-means Loop
for i in range(iterations):
    # Vectorized distance calculation
    dist = np.sum(pixels**2, axis=1, keepdims=True) - 2 * np.dot(pixels, centroids.T) + np.sum(centroids**2, axis=1)
    labels = np.argmin(dist, axis=1)
    
    # Update centroids
    new_centroids = np.array([pixels[labels == j].mean(axis=0) if np.any(labels == j) else centroids[j] for j in range(k)])
    
    if np.allclose(centroids, new_centroids, atol=0.5):
        break
    centroids = new_centroids

# Reshape labels back to original image dimensions
labels_2d = labels.reshape((h, w))

# Background Detection
# Collect labels from all four edges to decide which cluster is the background
top = labels_2d[0, :]
bottom = labels_2d[-1, :]
left = labels_2d[:, 0]
right = labels_2d[:, -1]
edges = np.concatenate([top, bottom, left, right])
bg_label = np.bincount(edges).argmax()

# Mask Optimization (Removing the "Thin Line")
# Initial binary mask: Background is white (255), Subject is black (0)
mask = np.where(labels_2d == bg_label, 255, 0).astype(np.uint8)

# We dilate the background mask slightly (shrunk the foreground) to remove edge halos
kernel = np.ones((3, 3), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=1) 

# Soften the edges using a Gaussian Blur
mask_soft = cv2.GaussianBlur(mask, (5, 5), 0).astype(float) / 255.0
alpha = cv2.merge([mask_soft, mask_soft, mask_soft])

# Final Composition (Alpha Blending)
# Result = (Background * Alpha) + (Foreground * (1 - Alpha))    [Module handles...]
foreground_part = cv2.multiply(img.astype(float), 1.0 - alpha)
background_part = cv2.multiply(bg.astype(float), alpha)
result = cv2.add(foreground_part, background_part).astype(np.uint8)

# Display Updated picture
cv2.imshow("Final Virtual Background", result)
cv2.waitKey(0)
cv2.destroyAllWindows()