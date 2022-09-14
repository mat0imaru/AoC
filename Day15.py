import numpy as np
from utils import readFileReturnMap
import cv2

# reccursive solver -> take too long time
def lowest_risk_level(m: np.ndarray, x: int, y: int) -> int:
    if (x == 0) and (y == 0):
        return 0
    elif (x == 0):
        return m[x][y] + lowest_risk_level(m, x, y-1)
    elif (y == 0):
        return m[x][y] + lowest_risk_level(m, x-1, y)
    else:
        return m[x][y] + min(lowest_risk_level(m, x-1, y), lowest_risk_level(m, x, y-1))

# conquering solver -> answer for sample. but, wrong answer for input
def risk_level(m: np.ndarray):
    width, height = np.shape(m)
    result = np.zeros_like(m)
    for i in range(width):
        for j in range(height):
            if (i == 0) and (j == 0):
                result[i][j] = 0
            elif (i == 0):
                result[i][j] = m[i][j] + result[i][j-1]
            elif (j == 0):
                result[i][j] = m[i][j] + result[i-1][j]
            else:
                result[i][j] = m[i][j] + min(result[i-1][j], result[i][j-1])
    return result

def main():
    width = 100
    height = 100
    f = open("Day15_input", 'r')
    chiton_map = readFileReturnMap(f, width, height)
    risk_level_map = risk_level(chiton_map)
    print(chiton_map)
    print(risk_level_map)
    print(risk_level_map[-1][-1])
    cv2.imshow("risk_level",cv2.resize(risk_level_map/np.max(risk_level_map), dsize=(400,400), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(0)


if __name__ == "__main__":
    main()