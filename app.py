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
_DATABASE_PATH = 'fingerprintColorImageDatabase.v1/'
_CDN_PATH = 'cdn/'


def threshold_apply(image):
    # Threshold (identify the white black pixel by near method and convert in white or black absolute)
    _, image = cv2.threshold(
        image, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # Normalize to 0 and 1 range
    image[image == 255] = 1
    return image

def convert_to_array(image):
    applyclahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image = applyclahe.apply(image)
    image = fingerprint_enhancer.enhance_Fingerprint(image)
    image = numpy.array(image, dtype=numpy.uint8)
    return image

def harris_corners_apply(image):
    # Harris corners
    harris_corners_arr = cv2.cornerHarris(image, 3, 3, 0.04)
    harris_normalized_arr = cv2.normalize(
        harris_corners_arr, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32FC1)
    return harris_normalized_arr

def extract_keypoint(harris_normalized_arr):
    keypoints = []
    for x in range(0, harris_normalized_arr.shape[0]):
        for y in range(0, harris_normalized_arr.shape[1]):
            if harris_normalized_arr[x][y] > _FRONTIER:
                keypoints.append(cv2.KeyPoint(y, x, 1))
    return keypoints

def calculate_score(matches):
    # Calculate score test
    score = 0
    for match in matches:
        score += match.distance
    if score/len(matches) < _ALLOW_ERROR_THRESHOLD:
        return True
    else:
        return False

def remove_file(filename):
    os.remove(_CDN_PATH + filename)

def get_descriptors(image):
    
    image = convert_to_array(image)
    image = threshold_apply(image)
    image_harries_normalized = harris_corners_apply(image)
    # Extract keypoints
    keypoints = extract_keypoint(image_harries_normalized)
    # Define descriptor
    orb = cv2.ORB_create()
    # Compute descriptors
    _, des = orb.compute(image, keypoints)
    return (keypoints, des)

def draw_points(images_list, kp_list, matches):
    # Plot keypoints
    image_keypoints_1 = cv2.drawKeypoints(images_list[0], kp_list[0], outImage=None)
    image_keypoints_2 = cv2.drawKeypoints(images_list[1], kp_list[1], outImage=None)
    s, arrax = plt.subplots(1, 2)
    arrax[0].imshow(image_keypoints_1)
    arrax[1].imshow(image_keypoints_2)
    plt.show()
    # Plot matches
    image_keypoints_3 = cv2.drawMatches(images_list[0], kp_list[0], images_list[1], kp_list[1], matches, flags=2, outImg=None)
    plt.imshow(image_keypoints_3)
    plt.show()

def compare_image(file):

    img1 = cv2.imread( _DATABASE_PATH + '/sub2/22.jpg', cv2.IMREAD_GRAYSCALE)
    # img1 = cv2.imread( _CDN_PATH + filename, cv2.IMREAD_GRAYSCALE)
    kp1, des1 = get_descriptors(img1)

    is_searching = True
    is_coinciding = False

    for dirName, subdirList, fileList in os.walk(_DATABASE_PATH):
        for filename in fileList:
            print( dirName + '/' + filename)
            img2 = cv2.imread( dirName + '/' + filename, cv2.IMREAD_GRAYSCALE)
            kp2, des2 = get_descriptors(img2)

            # Matching between descriptors
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = sorted(bf.match(des1, des2), key=lambda match: match.distance)
        
            # Draw points
            is_coinciding = calculate_score(matches) 

            if ( is_coinciding ):
                print('Coincide')
                is_searching = False
                break
            else:
                print('No Coincide')
                pass
            
        if  ( not is_searching ): 
            break

    # remove_file(file.name)
    return is_coinciding
                
        
if __name__ == "__main__":
    try:
        compare_image('')
    except:
        raise
