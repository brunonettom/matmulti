import numpy as np
import math 
# Definir uma função para verificar a primeira equação
def eq1(B):
    return np.isclose(6 * np.sin(B / 2), -7 * np.sin(3 * B / 2), atol=1e-5)

# Definir uma função para verificar a segunda equação
def eq2(A, B):
    return np.isclose(6 * np.sin(A / 2) * np.sin(B / 2), 7 * np.sin(3 * A / 2) * np.sin(3 * B / 2), atol=1e-5)

# Definir intervalo e discretização
A_vals = np.linspace(0, 4 * np.pi, 1000)  # 1000 pontos entre 0 e 4pi
B_vals = np.linspace(-2 * np.pi, 0, 1000)  # 1000 pontos entre -2pi e 0

# Lista para armazenar soluções
solucoes = []

# Iterar sobre os valores de A e B
for A in A_vals:
    for B in B_vals:
        # Verificar se o par (A, B) satisfaz as equações
        u = (A + B) / 2
        v = (A-B)/2

        # Cálculo de x e y com as fórmulas corretas
        xu = 6 * math.cos(u) - 7 * math.cos(3 * u)
        yu = 6 * math.sin(u) - 7 * math.sin(3 * u)
        if eq1(B) and eq2(A, B):
            
            solucoes.append((xu,yu))

print(solucoes)
