## A Watermelon 🍉
# Mubashir is eating a watermelon.
# He spits out all watermelon seeds if seeds are more than five.
# He can swallow all watermelon seeds if seeds are less than five.
# He can eat 1/4 of watermelon each time.
# Given a 2D array of watermelon where 0 is representing juicy watermelon while 1 is representing seed, return total number of seeds spit-out. See below example for detailed explanation:
# Given a watermelon:
# 1, 0, 0, 1, 1, 1, 0, 1
# 1, 0, 1, 0, 1, 1, 0, 0
# 1, 1, 1, 1, 0, 0, 0, 0
# 0, 1, 0, 1, 1, 1, 1, 0
# 0, 0, 0, 1, 0, 1, 0, 0
# 1, 1, 1, 0, 0, 0, 1, 1
# 1, 0, 1, 1, 0, 0, 0, 0
# 0, 0, 0, 0, 0, 0, 0, 0
# seeds = 0
# total seeds = 0

# Mubashir eats 1/4 piece (4x4 matrix) of watermelon :
# x, x, x, x, 1, 1, 0, 1
# x, x, x, x, 1, 1, 0, 0
# x, x, x, x, 0, 0, 0, 0
# x, x, x, x, 1, 1, 1, 0
# 0, 0, 0, 1, 0, 1, 0, 0
# 1, 1, 1, 0, 0, 0, 1, 1
# 1, 0, 1, 1, 0, 0, 0, 0
# 0, 0, 0, 0, 0, 0, 0, 0
# seeds = 10
# total seeds = 10 (All seeds were spit-out)

# Mubashir eats next 1/4 piece (4x4 matrix) of watermelon :
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# 0, 0, 0, 1, 0, 1, 0, 0
# 1, 1, 1, 0, 0, 0, 1, 1
# 1, 0, 1, 1, 0, 0, 0, 0
# 0, 0, 0, 0, 0, 0, 0, 0
# seeds = 8
# total seeds = 10+8 = 18 (All seeds were spit-out)

# Mubashir eats next 1/4 piece (4x4 matrix) of watermelon :
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, 0, 1, 0, 0
# x, x, x, x, 0, 0, 1, 1
# x, x, x, x, 0, 0, 0, 0
# x, x, x, x, 0, 0, 0, 0
# seeds = 7
# total seeds = 18+7 = 25 (All seeds were spit-out)

# Mubashir eats last 1/4 piece (4x4 matrix) of watermelon :
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# x, x, x, x, x, x, x, x
# seeds = 3
# total seeds = 25+0 = 25

## Examples
# total_seeds(watermelon) ➞ 25

import math
import numpy as np
from numpy.core.fromnumeric import nonzero

def total_seeds(watermelon):
    # convert to numpy
    watermelon = np.asarray(watermelon)

    # variables
    seeds = 0
    pieces = []

    # floor to not exceed 1/4 watermelon
    x_mat = math.floor(len(watermelon)/2)
    y_mat = math.floor(len(watermelon[0])/2)

    # add the four pieces that will always be there
    pieces.append(watermelon[0:x_mat,0:y_mat])
    pieces.append(watermelon[0:x_mat,y_mat:2*y_mat])
    pieces.append(watermelon[x_mat:2*y_mat,0:y_mat])
    pieces.append(watermelon[x_mat:2*x_mat,y_mat:2*y_mat])

    # consider the extra pieces
    if len(watermelon)%2==1 and len(watermelon[0])%2==1:
        pieces.append(watermelon[-1])
        pieces.append(watermelon[:,-1][0:-1])
    elif len(watermelon)%2==1:
        pieces.append(watermelon[-1])
    elif len(watermelon[0])%2==1:
        pieces.append(watermelon[:,-1])
    
    # count the number of seeds
    for piece in pieces:
        seeds_in_piece = np.count_nonzero(piece==1)
        if seeds_in_piece > 5:
            seeds += seeds_in_piece
    return seeds

watermelon1 = [[1,0,0,1,1,1,0,1],   # 8x8
               [1,0,1,0,1,1,0,0],
               [1,1,1,1,0,0,0,0],
               [0,1,0,1,1,1,1,0],
               [0,0,0,1,0,1,0,0],
               [1,1,1,0,0,0,1,1],
               [1,0,1,1,0,0,0,0],
               [0,0,0,0,0,0,0,0]]
watermelon2 = [[1,1,1,0,0,1,1,1,0], # 7x9
               [1,1,0,1,1,0,1,0,1],
               [1,1,1,1,1,0,0,1,1],
               [1,1,0,1,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [1,0,1,1,0,0,0,0,1],
               [1,0,0,0,1,0,0,1,0]]
watermelon3 = [[1,0,1,0,0,1,1],     # 8x7
               [0,0,0,1,1,1,0],
               [1,1,1,1,1,0,1],
               [1,1,1,1,0,0,0],
               [0,0,0,0,0,0,1],
               [1,0,1,1,0,1,1],
               [1,1,1,1,1,1,1],
               [0,0,0,0,0,0,0]]
watermelon4 = [[1,0,1,0,0,1,1,1],   # 7x8
               [0,0,0,1,1,0,1,0],
               [1,1,1,1,1,0,0,0],
               [1,1,1,1,0,0,0,0],
               [0,0,0,0,0,1,0,0],
               [1,0,1,1,0,1,0,0],
               [1,0,0,0,1,0,0,1]]
print(total_seeds(watermelon1))
print(total_seeds(watermelon2))
print(total_seeds(watermelon3))
print(total_seeds(watermelon4))