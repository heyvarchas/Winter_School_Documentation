import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot Open Camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?, Exiting ...")
        break

    bg_original = cv.imread("bg.jpg")

    # Get original dimensions
    h, w, _ = frame.shape

    # Resize background to match the original image size exactly
    bg = cv.resize(bg_original, (w, h))

    # Prepare Data (Flattening for K-means)
    pixels = frame.reshape((-1, 3)).astype(np.float32)

    k = 5  # Higher K helps isolate the "edge" colors from the subject [Set accordingly]
    iterations = 5
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

    # Background Detection (Perimeter Voting)
    # Collect labels from all four edges to decide which cluster is the background [Largest cluster is bg]
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
    mask = cv.dilate(mask, kernel, iterations=1) 

    # Soften the edges using a Gaussian Blur
    mask_soft = cv.GaussianBlur(mask, (5, 5), 0).astype(float) / 255.0
    alpha = cv.merge([mask_soft, mask_soft, mask_soft])

    # Final Composition (Alpha Blending)
    # Result = (Background * Alpha) + (Foreground * (1 - Alpha))    [Module Handles]
    foreground_part = cv.multiply(frame.astype(float), 1.0 - alpha)
    background_part = cv.multiply(bg.astype(float), alpha)
    result = cv.add(foreground_part, background_part).astype(np.uint8)

    cv.imshow('frame', result)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()