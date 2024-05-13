import cv2
import os

# Load the original fingerprint image
test_original = cv2.imread("C:/Users/Pashie/PycharmProjects/pythonProject/AuthenticationSystem/FingerprintDatabase/Fingerprint_001.jpeg")
cv2.imshow("Original", cv2.resize(test_original, None, fx=1, fy=1))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load the fingerprint database image
fingerprint_database_image = cv2.imread("C:/Users/Pashie/PycharmProjects/pythonProject/AuthenticationSystem/FingerprintDatabase/Fingerprint_002.jpeg")

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors for both images
keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

# Perform FLANN matching
matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_FLANNBASED)
matches = matcher.knnMatch(descriptors_1, descriptors_2, k=2)

# Filter good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Calculate matching score
matching_score = len(good_matches) / min(len(keypoints_1), len(keypoints_2)) * 100

# Display matching results
if matching_score > 95:
    print("% Match:", matching_score)
    print("Fingerprint ID: Fingerprint_001")

    # Draw matches and gives feedback
    result = cv2.drawMatches(test_original, keypoints_1, fingerprint_database_image, keypoints_2, good_matches, None)
    result = cv2.resize(result, None, fx=2.5, fy=2.5)

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Fingerprints do not match.")

