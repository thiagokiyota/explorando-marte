import numpy as np

# Criando o planalto
def base(x, y):
    a = np.zeros([x, y], dtype=int)
    return a

planalto = base(5, 5)
print(planalto)