import math
import numpy as np
pi = math.pi

def f(A, B):
    """
    Função para calcular f(A, B) com base na expressão trigonométrica.
    """
    resultado=6*math.cos(A/2)*math.sin(B/2) - 7*math.cos(3*A/2)*math.sin(3*B/2)
    # print(f'A:{A},B:{B},resultado:{resultado}')
    return resultado


def encontrar_intervalo(A, B_min, B_max, num_pontos=1000):
    """
    Encontra um intervalo [a, b] onde f(x) muda de sinal no intervalo [B_min, B_max].
    """
    x = np.linspace(B_min, B_max, num_pontos)
    for i in range(len(x) - 1):
        if f(A,x[i]) * f(A,x[i + 1]) < 0:
            # print(x[i], x[i + 1])
            return x[i], x[i + 1]
    return None, None

def bisseccao(A, B_min, B_max,tol=1e-7, max_iter=1000):
    """
    Função que implementa o método da bisseção para encontrar a raiz de f(x) = 0
    dentro do intervalo [a, b] com uma tolerância 'tol'.
    """
    
    a,b=encontrar_intervalo(A, B_min, B_max)

    # Loop principal de bisseção
    for i in range(max_iter):
        m = (a + b) / 2  # ponto médio
        if abs(f(A,m)) < tol or (b - a) / 2 < tol:
            return m  # retorna a raiz aproximada

        # Verifica em qual metade está a raiz
        if f(A,a) * f(A,m) < 0:
            b = m  # raiz está no intervalo [a, m]
        else:
            # print(m)
            
            a = m  # raiz está no intervalo [m, b]
    return m



# Testando a função adaptada com a função exemplo (x^2 - 4)



# Lista de valores de A
As = [0, pi, 2*pi, 4*pi]
listaAB = []

B_min, B_max = -2*pi,0
# Para cada valor de A, procurar as raízes de B
for A in As:
    B_min, B_max = -2*pi,0
   
    B = bisseccao(A, B_min, B_max,tol=1e-7, max_iter=1000)
    B
    # print(B)
    # print(A)
    listaAB.append([A,B])
    

def lista_AB_uv_xuvyuv(listaAB):
        
    lista_AB_uv_xuvyuv=[]
    str=''
    # print(listaAB)
    for AB in listaAB:
        A = AB[0]
        B = AB[1]
        # print('AB')
        
        u = (A + B) / 2
        v = (A-B)/2  
        # Cálculo de x e y com as fórmulas corretas
        
        xu = 6 * math.cos(u) - 7 * math.cos(3 * u)
        yu = 6 * math.sin(u) - 7 * math.sin(3 * u)
        xv = 6 * math.cos(v) - 7 * math.cos(3 * v)
        yv = 6 * math.sin(v) - 7 * math.sin(3 * v)

        bate=(abs(xu-xv)<0.01 and abs(yu-yv)<0.01)

        lista_AB_uv_xuvyuv.append([A,B,u,v,xu,xv,yu,yv,bate])
        str+=(f'A:{A:.1f}, B:{B:.1f} || u:{u:.1f}, v:{v:.1f},|| xu:{xu:.1f}, xv:{xv:.1f}|, yu:{yu:.1f}, yv:{yv:.1f}, ||bate:{bate} \n')
    return str

# lista_AB_uv_xuvyuv(listaAB)
print(lista_AB_uv_xuvyuv(listaAB))