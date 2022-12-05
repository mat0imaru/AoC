import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.zeros([4,4])

c = np.zeros([10,10,3])
for i in range(10):
    for j in range(10):
        c[i][j] = (i,j,i+j)

print(c)
for i in range(10):
    for j in range(10):
        if np.all(c[i][j] == (1,1,200)):
            print("true")
