import numpy as np
from utils import readFileReturnMap
import cv2
from functools import lru_cache
import time

np.printoptions(precision=0)

# # reccursive solver -> take too long time
# def lowest_risk_level(m: np.ndarray, x: int, y: int) -> int:
#     if (x == 0) and (y == 0):
#         return 0
#     elif (x == 0):
#         return m[x][y] + lowest_risk_level(m, x, y-1)
#     elif (y == 0):
#         return m[x][y] + lowest_risk_level(m, x-1, y)
#     else:
#         return m[x][y] + min(lowest_risk_level(m, x-1, y), lowest_risk_level(m, x, y-1))

# # conquering solver -> answer for sample. but, wrong answer for input
# def risk_level(m: np.ndarray):
#     width, height = np.shape(m)
#     result = np.zeros_like(m)
#     for i in range(width):
#         for j in range(height):
#             if (i == 0) and (j == 0):
#                 result[i][j] = 0
#             elif (i == 0):
#                 result[i][j] = m[i][j] + result[i][j-1]
#             elif (j == 0):
#                 result[i][j] = m[i][j] + result[i-1][j]
#             else:
#                 result[i][j] = m[i][j] + min(result[i-1][j], result[i][j-1])
#     return result

# # direction not be restict to down and right
# def lowest_risk_level2(m: np.ndarray, x, y):
#     if (x == 0) and (y == 0):
#         return 0
#     elif (x == 0):
#         return m[x][y] + lowest_risk_level(m, x, y-1)
#     elif (y == 0):
#         return m[x][y] + lowest_risk_level(m, x-1, y)
#     else:
#         return m[x][y] + min(lowest_risk_level(m, x-1, y), lowest_risk_level(m, x, y-1))

# # greedy solver
# def greedy_lowest_risk_level(m: np.ndarray):
#     odom = []
#     restricted = []
#     w, h = np.shape(m)
#     pos = (0,0)
#     total_risk_level = 0
#     while not pos == (w-1,h-1):
#         # time.sleep(0.1)
#         print(pos)
#         odom.append(pos)
#         # print(f"odom = {odom}")
#         actions = available_actions(pos, w, h)
#         next_poses = []
#         for act in actions:
#             next_pos = (pos[0]+act[0],pos[1]+act[1])
#             if not next_pos in restricted:
#                 if not next_pos in odom:
#                     next_poses.append(next_pos)
#         # print(f"next_poses = {next_poses}")
#         # print(f"restricted = {restricted}")
#         if len(next_poses) == 0:
#             restricted.append(odom.pop())
#             if pos == odom[-1]:
#                 odom.pop()
#             pos = odom[-1]
#             continue
#             # print("trapped!!!")
#             # return 99999999999, odom
#         min_risk_idx = -1
#         min_risk_level = 100
#         for i,next_p in enumerate(next_poses):
#             risk_level = m[next_p[0],next_p[1]]
#             if risk_level < min_risk_level:
#                 min_risk_idx = i
#                 min_risk_level = risk_level
#         total_risk_level += min_risk_level
#         pos = next_poses[min_risk_idx]
#     return total_risk_level, odom

# def available_actions(pos, width, height):
#     actions = [(1,0),(0,1),(-1,0),(0,-1)]
#     if pos[1] < 1:
#         actions.pop(3)
#     if pos[0] < 1:
#         actions.pop(2)
#     if pos[1] > width-2:
#         actions.pop(1)
#     if pos[0] > height-2:
#         actions.pop(0)
#     return actions

# dijkstra solver
def dijkstra_lowest_risk_level(m, w, h):
    w, h = np.shape(m)
    visited = []
    visited_map = np.zeros_like(m)
    risk_level_map = np.ones_like(m)*1000000
    risk_level_map[0,0] = 0
    current_pos = 0
    while not current_pos == 9999:
        reachable = available_node(current_pos, w, h)
        # print(reachable)
        for r in reachable:
            if r in visited:
                continue
            distance = risk_level_map[current_pos//w, current_pos%h] + m[r//w, r%h]
            print(f"now_pos = {current_pos}, next_pos = {r}, distance = {distance}")
            # print(f"risk level of next_pos = {risk_level_map[r//100, r%100]}")
            if distance < risk_level_map[r//w, r%h]:
                risk_level_map[r//w, r%h] = distance
        visited.append(current_pos)
        visited_map[current_pos//w, current_pos%h] = 1000000
        # print(visited_map+risk_level_map)
        current_pos = np.argmin(visited_map+risk_level_map)
        if current_pos == w*h-1:
            break
        # time.sleep(0.05)
        cv2.imshow("risk_level",cv2.resize(risk_level_map/np.max(risk_level_map), dsize=(600,600), interpolation=cv2.INTER_NEAREST))
        # cv2.imshow("visited",cv2.resize(visited_map/np.max(visited_map), dsize=(600,600), interpolation=cv2.INTER_NEAREST))
        cv2.waitKey(1)
    return risk_level_map

def available_node(pos, w, h):
    nodes = []
    if (pos+1)//w == (pos//w):
        nodes.append(pos+1)
    if pos//w < 99:
        nodes.append(pos+w)
    if pos-w >= 0:
        nodes.append(pos-w)
    if (pos%w)-1 >= 0:
        nodes.append(pos-1)
    return nodes

def map_extender(m):
    w, h = np.shape(m)
    extended = np.zeros((5*w, 5*h))
    for i in range(w):
        for j in range(h):
            risk_level = m[i,j]
            for k in range(5):
                for l in range(5):
                    extended[i*k, j*l] = (risk_level+k+l)%10
    return extended

def main():
    width = 100
    height = 100
    f = open("Day15_input", 'r')
    chiton_map = readFileReturnMap(f, width, height)
    ext_chiton_map = map_extender(chiton_map)
    risk_level_map = dijkstra_lowest_risk_level(ext_chiton_map, width*5, height*5)

    # risk_level, odom = greedy_lowest_risk_level(chiton_map)
    # print(risk_level)
    # print(odom)
    
    # odom_map = np.zeros((200,200))
    # for o in odom:
    #     odom_map[o[0]*2,o[1]*2] = 255

    # cv2.imshow("odometry", cv2.resize(odom_map/np.max(odom_map), dsize=(400,400)))
    # cv2.waitKey(0)

    # risk_level_map = risk_level(chiton_map)
    #print(chiton_map)
    # print(risk_level_map)
    print(f"risk level = {risk_level_map[-1][-1]}")
    # cv2.imshow("risk_level",cv2.resize(risk_level_map/np.max(risk_level_map), dsize=(600,600), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(0)

if __name__ == "__main__":
    main()