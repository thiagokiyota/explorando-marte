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
area = input()

# Tratamento das entradas
area = area.split()

# Considerando que na perspectiva do usuario o tamanho do planalto vai ter 5 posicoes de 0 a 5 estou incrementando a area para atender a essa expectativa
largura_plano = int(area[0])
altura_plano = int(area[1])
largura_plano = largura_plano + 1
altura_plano = altura_plano + 1

# Criacao do planalto
planalto = base(largura_plano, altura_plano)

# Posição inicial da sonda1
# planalto[x, y] = 1

# print("Posicao inicial da sonda1: ", x1, y1, z1)
# print("Posicao inicial da sonda2: ", x2, y2, z2)

# Movimentos da sonda1
def movimenta_sonda(comandos, x, y, z):
    for mov in comandos:
        if mov == 'M':
            posicao_final = mover(x, y, z)
            if posicao_final[0] < largura_plano and posicao_final[1] < altura_plano:
                x = int(posicao_final[0])
                y = int(posicao_final[1])
            else:
                raise Exception("Movimento inválido, sem execução")
        else:
            z = rotate(z, mov)

    planalto[x, y] = 1
    print(x, y, z)

entrada = input("Digite a posição da nova sonda ou CTRL + C\n")

while entrada != "S":
    entrada = entrada.split()
    x1 = int(entrada[0])
    y1 = int(entrada[1])
    z1 = entrada[2].upper()
    movimentos = []
    movimentos[:0] = input()
    movimenta_sonda(movimentos, x1, y1, z1)
    entrada = input("Digite a posição da nova sonda ou CTRL + C\n")

# print(np.rot90(planalto))
