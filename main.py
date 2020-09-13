import numpy as np

def DFS_Matrix(start):
    global data, data_shape, curcuit
    for i in range(data_shape[1]):
        if data[start][i] != 0:
            data[start][i] = data[i][start] = 0
            DFS_Matrix(i)
    curcuit.append(start)

if __name__=="__main__":
    global data, data_shape, curcuit
    data = np.array([[0, 1, 0, 0, 1, 0],
                     [1, 0, 1, 1, 1, 0],
                     [0, 1, 0, 1, 0, 0],
                     [0, 1, 1, 0, 1, 1],
                     [1, 1, 0, 1, 0, 0],
                     [0, 0, 0, 1, 0, 0]])
    data_shape = data.shape
    curcuit = []

    even_pos = np.where(data.sum(axis=1) % 2 == 1)[0]
    if len(even_pos) == 0:
        DFS_Matrix(0)
    else:
        data[even_pos[1]][even_pos[0]] = data[even_pos[0]][even_pos[1]] = 1
        DFS_Matrix(0)
        for i in range(len(curcuit)-1):
            if (curcuit[i:i + 2] == list(even_pos) or
                curcuit[i:i + 2] == list(reversed(even_pos))):
                curcuit = curcuit[i + 1:-1] + curcuit[:i + 1]
    print(curcuit)

