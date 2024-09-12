import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi

def f(A, B):
    """
    Função para calcular f(A, B) com base na expressão trigonométrica.
    """
    return 6 * math.cos(A / 2) * math.sin(B / 2) - 7 * math.cos(3 * A / 2) * math.sin(3 * B / 2)

def df(A, B, h=1e-8):
    """
    Aproximação numérica da derivada de f(A, B) com relação a B usando o método das diferenças finitas.
    
    Parâmetros:
    A -- Valor fixo de A.
    B -- Valor de B onde queremos calcular a derivada.
    h -- Pequena variação para aproximar a derivada (padrão: 1e-8).
    
    Retorno:
    Aproximação de f'(A, B).
    """
    return (f(A, B + h) - f(A, B)) / h

def newton(A, B0, tol=1e-8, max_iter=200):
    """
    Função para encontrar a raiz de f(A, B) usando o método de Newton.

    Parâmetros:
    A         -- Valor fixo de A.
    B0        -- Chute inicial para o valor de B.
    tol       -- Tolerância para o critério de parada (padrão: 1e-8).
    max_iter  -- Número máximo de iterações permitidas (padrão: 200).

    Retorno:
    Aproximação da raiz de f(A, B) dentro da tolerância.
    """
    B = B0

    for _ in range(max_iter):
        f_val = f(A, B)
        df_val = df(A, B)
        
        # Aplicar o método de Newton: B_novo = B - f(B) / f'(B)
        if abs(df_val) < 1e-100:  # Evitar divisão por valores muito pequenos
            break  # Evitar divisão por zero, caso a derivada seja nula
        
        B_novo = B - f_val / df_val
        
        # Se a diferença entre o valor antigo e o novo for menor que a tolerância, paramos
        if abs(B_novo - B) < tol:
            return B_novo
        
        B = B_novo
    
    return B

# Lista de valores de A
As = [0, pi / 2, pi, 3 * pi / 2]
vuxys = []

# Para cada valor de A, procurar as raízes de B usando o método de Newton
for A in As:


    B = newton(A, (-2*pi) / 2, tol=1e-80, max_iter=20000)

    # Cálculo de u (média de A e B)
    u = (A + B) / 2
    v = (A-B)/2

    # Cálculo de x e y com as fórmulas corretas
    xu = 6 * math.cos(u) - 7 * math.cos(3 * u)
    yu = 6 * math.sin(u) - 7 * math.sin(3 * u)
    xv = 6 * math.cos(v) - 7 * math.cos(3 * v)
    yv = 6 * math.sin(v) - 7 * math.sin(3 * v)
    # Arredondando valores de x e y
    vuxys.append([[v,u],[[round(xv, 3), round(yv, 3)],[round(xu, 3), round(yu, 3)]]])
    

# Imprimir as raízes encontradas
result = '\n'.join([f'v:{vuxy[0][1]:.3f} | u:{vuxy[0][0]:.3f} ||| xv:{vuxy[1][0][0]:.3f} | yv:{vuxy[1][0][1]:.3f} || xu:{vuxy[1][1][0]:.3f} | yu:{vuxy[1][1][1]:.3f} || ' for vuxy in vuxys])
print(result)