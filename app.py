import numpy as np

def base(x, y):
    a = np.zeros([x, y], dtype=int)
    return a

def rotate(direction, side):
    compass = np.array(['N', 'E', 'S', 'W'])
    result = np.where(compass == direction)
    
    if side == 'L':
        if int(result[0]) > 0:
            rotate = compass[int(result[0]) -1]
            return rotate
        else:
            rotate = compass[3]
            return rotate
    elif side == 'R':
        if int(result[0]) < 3:
            rotate = compass[int(result[0]) + 1]
            return rotate
        else:
            rotate = compass[0]
            return rotate

def mover(x, y, z):
    if z == 'N':
        new = [x, y+1, z]
        return new
    
    if z == 'E':
        new = [x+1, y, z]
        return new

    if z == 'S':
        new = [x, y-1, z]
        return new

    if z == 'W':
        new = [x-1, y, z]
        return new
    
# Parametros de entrada
area = "6 5"
sonda1 = "1 2 N"
movimentos1 = []
movimentos1[:0] = 'LMLMLMLMM'

sonda2 = "3 3 E"
movimentos2 = []
movimentos2[:0] = 'MMRMMRMRRM'

# Tratamento das entradas
area = area.split()
p1 = int(area[0])
p2 = int(area[1])

sonda1 = sonda1.split()
x1 = int(sonda1[0])
y1 = int(sonda1[1])
z1 = sonda1[2].upper()

sonda2 = sonda2.split()
x2 = int(sonda2[0])
y2 = int(sonda2[1])
z2 = sonda2[2].upper()

# Criacao do planalto
planalto = base(p1, p2)

# Posição inicial da sonda1
# planalto[x, y] = 1

print("Posicao inicial da sonda1: ", x1, y1, z1)
print("Posicao inicial da sonda2: ", x2, y2, z2)

# Movimentos da sonda1
for mov in movimentos1:
    if mov == 'M':
        aux = mover(x1, y1, z1)
        x1 = int(aux[0])
        y1 = int(aux[1])
        
    else:
        z1 = rotate(z1, mov)

planalto[x1, y1] = 1
print("final sonda1", x1, y1, z1)

# Movimentos da sonda2
for mov in movimentos2:
    if mov == 'M':
        aux = mover(x2, y2, z2)
        x2 = int(aux[0])
        y2 = int(aux[1])
        
    else:
        z2 = rotate(z2, mov)

planalto[x2, y2] = 2
print("final sonda2", x2, y2, z2)

print(planalto)
