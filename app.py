# Python dependencies
import cv2
import os
import sys
import numpy

# Python libraries
import matplotlib.pyplot as plt
import fingerprint_enhancer

os.chdir("./")

_FRONTIER = 125  # Define frontier when the filtered image have color pixel white or black
_ALLOW_ERROR_THRESHOLD = 10


def get_descriptors(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img = clahe.apply(img)
    img = fingerprint_enhancer.enhance_Fingerprint(img)
    img = numpy.array(img, dtype=numpy.uint8)

    # Threshold (identify the white black pixel by near method and convert in white or black absolute)
    ret, img = cv2.threshold(
        img, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # Normalize to 0 and 1 range
    img[img == 255] = 1

    # Harris corners
    harris_corners = cv2.cornerHarris(img, 3, 3, 0.04)
    harris_normalized = cv2.normalize(
        harris_corners, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32FC1)
    threshold_harris = _FRONTIER

    # Extract keypoints
    keypoints = []
    for x in range(0, harris_normalized.shape[0]):
        for y in range(0, harris_normalized.shape[1]):
            if harris_normalized[x][y] > threshold_harris:
                keypoints.append(cv2.KeyPoint(y, x, 1))
    # Define descriptor
    orb = cv2.ORB_create()
    # Compute descriptors
    _, des = orb.compute(img, keypoints)
    return (keypoints, des)


def main():
    # for filename in os.listdir('database/'):
    #     print(filename)

    image_name = '103_1.jpg'
    img1 = cv2.imread("database/" + image_name, cv2.IMREAD_GRAYSCALE)
    kp1, des1 = get_descriptors(img1)

    image_name = '104_2.bmp'
    img2 = cv2.imread("database/" + image_name, cv2.IMREAD_GRAYSCALE)
    kp2, des2 = get_descriptors(img2)

    # Matching between descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = sorted(bf.match(des1, des2), key=lambda match: match.distance)

    # Plot keypoints
    # img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
    # img5 = cv2.drawKeypoints(img2, kp2, outImage=None)
    # f, axarr = plt.subplots(1, 2)
    # axarr[0].imshow(img4)
    # axarr[1].imshow(img5)
    # plt.show()
    # # Plot matches
    # img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
    # plt.imshow(img3)
    # plt.show()

    # Calculate score test
    score = 0
    for match in matches:
        score += match.distance
    score_threshold = _ALLOW_ERROR_THRESHOLD
    if score/len(matches) < score_threshold:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        main()
    except:
        raise
