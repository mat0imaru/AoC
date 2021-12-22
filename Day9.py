import numpy as np
import cv2
from utils import readFileReturnMap, sign
from time import sleep

def convolution(map, filter, fx = 3, fy = 3, padding = 1, stride = 1, const_val = 0):
    (width, height) = np.shape(map)
    padded_map = np.pad(map,((padding,padding),(padding,padding)), mode='constant',constant_values = const_val)
    output = np.zeros([int((width+2*padding-fx)/stride)+1,int((height+2*padding-fy)/stride)+1])
    for i in range(0,width,stride):
        for j in range(0,height,stride):
            filter_input = padded_map[i:i+fx,j:j+fy]
            output[i][j] = filter(filter_input)
    return output

def local_minimum(map):
    return  (sign(map[1][0] - map[1][1]) 
            & sign(map[1][2] - map[1][1])
            & sign(map[0][1] - map[1][1])
            & sign(map[2][1] - map[1][1]))

def main1():
    width = 100
    height = 100
    f = open("Day9_input",'r')
    map = readFileReturnMap(f, width, height)
    cv2.imshow('map', cv2.resize(map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST)/25)
    cv2.waitKey(0)
    low_point_map = np.zeros([width,height])
    for i in range(width):
        for j in range(height):
            if (i,j) == (0,0):
                low_point_map[i][j] =(sign(map[i+1][j] - map[i][j])
                                    & sign(map[i][j+1] - map[i][j]))
            elif (i,j) == (width-1,0):
                low_point_map[i][j] =(sign(map[i-1][j] - map[i][j])
                                    & sign(map[i][j+1] - map[i][j]))
            elif (i,j) == (0,height-1):
                low_point_map[i][j] =(sign(map[i+1][j] - map[i][j]) 
                                    & sign(map[i][j-1] - map[i][j]))
            elif (i,j) == (width-1,height-1):
                low_point_map[i][j] =(sign(map[i-1][j] - map[i][j]) 
                                    & sign(map[i][j-1] - map[i][j]))
            elif i == 0:
                low_point_map[i][j] =(sign(map[i+1][j] - map[i][j])
                                    & sign(map[i][j-1] - map[i][j])
                                    & sign(map[i][j+1] - map[i][j]))
            elif i == width-1:
                low_point_map[i][j] =(sign(map[i-1][j] - map[i][j])
                                    & sign(map[i][j-1] - map[i][j])
                                    & sign(map[i][j+1] - map[i][j]))
            elif j == 0:
                low_point_map[i][j] =(sign(map[i+1][j] - map[i][j])
                                    & sign(map[i-1][j] - map[i][j])
                                    & sign(map[i][j+1] - map[i][j]))
            elif j == height-1:
                low_point_map[i][j] =(sign(map[i-1][j] - map[i][j])
                                    & sign(map[i][j-1] - map[i][j])
                                    & sign(map[i+1][j] - map[i][j]))
            else:
                low_point_map[i][j] =(sign(map[i+1][j] - map[i][j]) 
                                    & sign(map[i][j+1] - map[i][j])
                                    & sign(map[i-1][j] - map[i][j])
                                    & sign(map[i][j-1] - map[i][j]))
    cv2.imshow('low_points', cv2.resize(low_point_map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    risk_map = np.zeros([width,height,3])
    risk_level = 0
    for i in range(width):
        for j in range(height):
            if low_point_map[i][j] == 1:
                risk_level += map[i][j]+1
                risk_map[i][j] = (0,0,255)
            else:
                risk_map[i][j] = np.array([1,1,1])*map[i][j]/25
    cv2.imshow('risk_level', cv2.resize(risk_map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(0)
    print(risk_level)

def main():
    width = 100
    height = 100
    f = open("Day9_input",'r')
    map = readFileReturnMap(f, width, height)
    o_map = np.copy(map)
    #cv2.imshow('map', cv2.resize(map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST)/25)
    #cv2.waitKey(0)
    low_point_map = convolution(map, local_minimum, const_val=9)
    #cv2.imshow('low_points', cv2.resize(low_point_map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST))
    #cv2.waitKey(0)
    risk_map = np.zeros([width,height,3])
    risk_level = 0
    risks = 0
    for i in range(width):
        for j in range(height):
            if low_point_map[i][j] == 1:
                risk_level += map[i][j]+1
                risks += 1
                risk_map[i][j] = (0,0,255)
            else:
                risk_map[i][j] = np.array([1,1,1])*map[i][j]/25
    #cv2.imshow('risk_level', cv2.resize(risk_map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST))
    #cv2.waitKey(0)
    print("risk_level = %d"% risk_level)
    basin_map = np.zeros([width,height,3], dtype=np.int)
    colors = []
    for i in range(width):
        for j in range(height):
            basin_map[i][j] = (0,0,0) if (o_map[i][j] == 9) else (255,255,255)
            if low_point_map[i][j] == 1:
                color = (int(255-i/100*255),int(255-200*abs(i-j)/100),int(j/100*255))
                basin_map[i][j] = color
                colors.append(color)
    cv2.imshow('basin_map', cv2.resize(basin_map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST)/255)
    cv2.waitKey(1)
    basin_map = np.pad(basin_map, ((1,1),(1,1),(0,0))) 
    colored = 0
    while not colored:
        colored = 1 
        for i in range(1,width+1):
            for j in range(1,height+1):
                surr = []
                surr.append(basin_map[i][j-1]) # up
                surr.append(basin_map[i][j+1]) # down
                surr.append(basin_map[i-1][j]) # left
                surr.append(basin_map[i+1][j]) # right
                if np.all(basin_map[i][j] == 255):
                    colored = 0
                    for s in surr:
                        if not (np.all(s == 255) or np.all(s == 0)):
                            basin_map[i][j] = s
        cv2.imshow('basin_map', cv2.resize(basin_map[1:width+1, 1:height+1, :],dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST)/255)
        cv2.waitKey(1)
    basin_map = basin_map[1:width+1, 1:height+1, :]
    cv2.imshow('basin_map', cv2.resize(basin_map,dsize=(0,0), fx=10, fy=10, interpolation=cv2.INTER_NEAREST)/255)
    cv2.waitKey(0)
    basin_size = [0]*len(colors)
    for i in range(width):
        for j in range(height):
            if not np.all(basin_map[i][j] == 0):
                basin_size[colors.index(tuple(basin_map[i][j]))] += 1
    print(basin_size)
    a = basin_size.pop(basin_size.index(max(basin_size)))
    b = basin_size.pop(basin_size.index(max(basin_size)))
    c = basin_size.pop(basin_size.index(max(basin_size)))
    print("Three largest basin sizes = %d, %d, %d, and its multiple = %d"%(a,b,c,a*b*c))

if __name__ == '__main__':
    main()