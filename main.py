import os
import time
import numpy as np
from scipy.signal import convolve2d

num = 10
cells = np.random.randint(0, 2, (num, num))

def view(lis):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[i][j] == 1:
                print('■', end='  ')
            else:
                print('.', end='  ')
        print('\n')
   
def count_neighb(grid):
    d = (-1, 0, 1)
    total_neighb = np.zeros((num, num), dtype=int)
    for dx in d:
        for dy in d:
            if dx == 0 and dy == 0:
                continue
            shift_grid = np.roll(grid, shift=(dx,dy), axis=(0,1))
            total_neighb +=shift_grid
    return total_neighb


def count_neighb_v2(grid):
    kernel = np.array([[1, 1, 1],     #ядро для прокатки
                       [1, 0, 1],
                       [1, 1, 1]])
    return convolve2d(grid, kernel, mode = 'same', boundary='wrap')
    

    
while True:
    os.system('cls')
    view(cells)
    cnt = count_neighb_v2(cells)
    
    birth = (cells == 0) & (cnt == 3) #побитовое сравнение для двух матриц
    survive = (cells == 1) & ((cnt == 2) | (cnt == 3))
    next_cells = birth | survive #побитовое или для двух матриц, то есть для каждой ячейки будет сравнение с другой ячейкой на том же месте
    
    
    cells = next_cells.astype(int)
    time.sleep(0.2)