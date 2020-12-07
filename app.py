import numpy as np

def base(x, y):
    a = np.zeros([x, y], dtype=int)
    return a

def rotate(direction, side):
    compass = np.array(['N', 'E', 'S', 'W'])
    result = np.where(compass == direction)
    
    if side == 'L':
        if result[0] > 0:
            rotate = compass[result[0] - 1]
            return rotate
        else:
            rotate = compass[3]
            return rotate
    elif side == 'R':
        if result[0] < 3:
            rotate = compass[result[0] + 1]
            return rotate
        else:
            rotate = compass[0]
            return rotate
