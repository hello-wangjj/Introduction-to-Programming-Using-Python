import cv2
import numpy as np


def main():
    pass


if __name__ == '__main__':
    # params for ShiTomasi corner detection
    feature_params = dict(maxCorners=100,
                          qualityLevel=0.3,
                          minDistance=7,
                          blockSize=7)

    # Parameters for lucas kanade optical flow
    lk_params = dict(winSize=(15, 15),
                     maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # Create some random colors
    color = np.random.randint(0, 255, (100, 3))
    start_img = cv2.imread('images/140 fps-000002.bmp')
    later_img = cv2.imread('images/140 fps-000003.bmp')
    old_gray = cv2.cvtColor(start_img, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
    # Create a mask image for drawing purposes
    mask = np.zeros_like(start_img)
    frame_gray = cv2.cvtColor(later_img, cv2.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv2.circle(later_img, (a, b), 5, color[i].tolist(), -1)
    img = cv2.add(later_img, mask)
    cv2.imwrite('Sparse.jpg', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        cv2.destroyAllWindows()
