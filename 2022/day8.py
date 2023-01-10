import numpy as np
import cv2
from utils import readFileReturnMap

if __name__ == "__main__":
    part = 2
    map = []
    width = 98
    height = width
    with open("day8_input", 'r') as f:
        map = readFileReturnMap(f, width+1, height+1)
    print(map)
    if part == 1:
        visibleMap = np.zeros_like(map)
        visibleMap[0,:] = 1
        visibleMap[width,:] = 1
        visibleMap[:,0] = 1
        visibleMap[:,height] = 1
        print(visibleMap)
        scale = 3
        cv2.imshow("visibleMap", cv2.resize(visibleMap,dsize=(0,0),fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST).transpose())
        cv2.waitKey(1)
        for i in range(1, width):
            for j in range(1, height):
                up = map[0:i,j]
                upmost = max(up)
                down = map[i+1:height+1,j]
                downmost = max(down)
                left = map[i,0:j]
                leftmost = max(left)
                right = map[i,j+1:width+1]
                rightmost = max(right)
                print(f"up:{upmost}, down:{downmost}, left:{leftmost}, right:{rightmost}")
                h = map[i,j]
                if h > min([upmost, downmost, leftmost, rightmost]):
                    print("visible")
                    visibleMap[i,j] = 1
                cv2.imshow("visibleMap", cv2.resize(visibleMap,dsize=(0,0),fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST))
                cv2.waitKey(1)
        print(np.unique(visibleMap, return_counts=True))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit()
    else:
        highest_scenic_score = 0
        for i in range(1, width):
            for j in range(10, height):
                up = map[0:i,j]
                down = map[i+1:height+1,j]
                left = map[i,0:j]
                right = map[i,j+1:width+1]
                h = map[i,j]
                upview = 0
                for u in up[::-1]:
                    upview += 1
                    if u >= h:
                        break
                downview = 0
                for d in down:
                    downview += 1
                    if d >= h:
                        break
                leftview = 0
                for l in left[::-1]:
                    leftview += 1
                    if l >= h:
                        break
                rightview = 0
                for r in right:
                    rightview += 1
                    if r >= h:
                        break
                # print(f"h = {h}, {up[::-1]},{down},{left[::-1]},{right}")
                # print(f"{upview},{downview},{leftview},{rightview}")
                scenic_score = upview*downview*leftview*rightview
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score
        print(highest_scenic_score)