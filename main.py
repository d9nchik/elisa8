from random import random

N = int(input("Введите размерность матрицы: "))
matrix = [0] * N
for x in range(N):
    matrix[x] = [0] * N


def setArray(matrix, size):
    for i in range(size):
        for j in range(size):
            matrix[i][j] = (int(random() * 10))


setArray(matrix, N)
print(matrix)
new = []


def maxArray(array):
    maxElement=array[0]
    for x in range (1, len(array)):
        if array[x] > maxElement:
            maxElement=array[x]
    return  maxElement

def setNew(matrix, size, new):

    for i in range(size):
        for j in range(size):
            if i < N-1:
                searchData = []
                tempI1 = i
                tempJ1 = j
                while tempI1 < (N - 1) and tempJ1 >= 0:
                    tempI = tempI1 + 1
                    while tempI < N:
                        searchData.append(matrix[tempI][tempJ1])
                        tempI = tempI + 1
                    tempI1 = tempI1 + 1
                    tempJ1 = tempJ1 - 1
                tempI1 = i + 1
                tempJ1 = j + 1
                while tempI1 < (N - 1) and tempJ1 < N:
                    tempI = tempI1 + 1
                    while tempI < N:
                        searchData.append(matrix[tempI][tempJ1])
                        tempI = tempI + 1
                    tempI1 = tempI1 + 1
                    tempJ1 = tempJ1 + 1
                print(searchData)
            else:
                searchData = []
                tempI1 = i
                tempJ1 = j
                while tempI1 >= 0 and tempJ1 >= 0:
                    tempI = tempI1 + 1
                    while tempI < N:
                        searchData.append(matrix[tempI][tempJ1])
                        tempI = tempI + 1
                    tempI1 = tempI1 - 1
                    tempJ1 = tempJ1 - 1
                tempI1 = i
                tempJ1 = j
                while tempI1 >= 0 and tempJ1 < N:
                    tempI = tempI1 + 1
                    while tempI < N:
                        searchData.append(matrix[tempI][tempJ1])
                        tempI = tempI + 1
                    tempI1 = tempI1 - 1
                    tempJ1 = tempJ1 + 1
                print(searchData)
            new[i][j]=maxArray(searchData)

rawin =[0]*N
for x in range (N):
    rawin[x]=[0]*N

setNew(matrix, N, rawin)
print(rawin)