import math
import numpy as np
pi = math.pi

def f(A, B):
    """
    Função para calcular f(A, B) com base na expressão trigonométrica.
    """
    return 6*math.cos(A/2)*math.sin(B/2) - 7*math.cos(3*A/2)*math.sin(3*B/2)

def bissecante(A, a, b, tol=1e-5, max_iter=100):
    """
    Função para encontrar a raiz de f(A, B) usando o método da bissecante.

    Parâmetros:
    A         -- Valor fixo de A.
    a         -- Extremo esquerdo do intervalo inicial para B.
    b         -- Extremo direito do intervalo inicial para B.
    tol       -- Tolerância para o critério de parada (padrão: 1e-5).
    max_iter  -- Número máximo de iterações permitidas (padrão: 100).

    Retorno:
    Aproximação da raiz de f(A, B) dentro da tolerância.
    """
    for _ in range(max_iter):
        fa = f(A, a)
        fb = f(A, b)
        # Fórmula da bissecante para encontrar novo ponto
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(A, c)

        # Se o valor de f(A, c) for pequeno o suficiente, retornamos a raiz
        if abs(fc) < tol:
            return c

        # Atualizar os valores de a ou b com base no sinal de f(A, c)
        if fa * fc < 0:
            b = c
        else:
            a = c
    
    return c

# Lista de valores de A
As = [0, pi, 2*pi, 4*pi]
A_Bs = []

# Para cada valor de A, procurar as raízes de B
for A in As:
    a = -2 * pi
    b = 2 * pi
    B_anterior = a

    # Varre o intervalo para encontrar onde há troca de sinal
    for B in np.arange(a, b, 0.5):
        if f(A, B_anterior) * f(A, B) < 0:  # Troca de sinal detectada
            raiz = bissecante(A, B_anterior, B, tol=1e-5, max_iter=100)
            A_Bs.append([A, raiz])
        
        B_anterior = B  # Atualizar o valor de B_anterior

# Imprimir as raízes encontradas
print(A_Bs)
