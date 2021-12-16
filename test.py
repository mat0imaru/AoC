import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.zeros([4,4])

for i in range(3):
    for j in range(3):
        b[i][j] = a[i][j]

print(b)