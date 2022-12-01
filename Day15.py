import numpy as np
from utils import readFileReturnMap
import cv2
from functools import lru_cache
import time

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
def dijkstra_lowest_risk_level(m):
    risk_level = 0
    risk_level_map = np.ones_like(m)*10000
    risk_level_map[0,0] = 0
    current_pos = 0
    reachable = available_node(current_pos)
    print(reachable)
    # print(risk_level_map)
    return risk_level

def available_node(pos):
    nodes = []
    if (pos+1)%100 == (pos%100):
        nodes.append(pos+1)
    if pos%100 < 99:
        nodes.append(pos+100)
    if pos-100 >= 100:
        nodes.append(pos-100)
    if pos-1 >= 0:
        nodes.append(pos-1)
    return nodes

def main():
    width = 100
    height = 100
    f = open("Day15_input", 'r')
    chiton_map = readFileReturnMap(f, width, height)
    dijkstra_lowest_risk_level(chiton_map)

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
    #print(risk_level_map)
    # print(risk_level_map[-1][-1])
    # cv2.imshow("risk_level",cv2.resize(risk_level_map/np.max(risk_level_map), dsize=(400,400), interpolation=cv2.INTER_NEAREST))
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()