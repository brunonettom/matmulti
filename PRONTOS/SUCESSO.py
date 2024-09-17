import math
import numpy as np
pi = math.pi

def f1(A, B): #função definida a partir de x
    """
    Função para calcular f1(A, B) com base na expressão trigonométrica.
    """
    resultado=6*math.cos(A/2)*math.sin(B/2) - 7*math.cos(3*A/2)*math.sin(3*B/2)
    return resultado

def f2(A, B): #função definida a partir de y
    """
    Função para calcular f2(A, B) com base na expressão trigonométrica.
    """
    resultado=6*math.sin(A/2)*math.sin(B/2) - 7*math.sin(3*A/2)*math.sin(3*B/2)
    return resultado


def encontrar_intervalo(f, A, B_min, B_max, num_pontos=1000):
    """
    Encontra um intervalo [a, b] onde f(x) muda de sinal no intervalo [B_min, B_max].
    """
    x = np.linspace(B_min, B_max, num_pontos)
    for i in range(len(x) - 1):
        if f(A,x[i]) * f(A,x[i + 1]) < 0:
            # print(x[i], x[i + 1])
            a = x[i]
            b = x[i+1]

            return a,b
    return None, None
tol=1e-10

def bisseccao(f,A, B_min, B_max):
    """
    Função que aplica o método da bisseção para encontrar a raiz de f(x) = 0
    dentro do intervalo [a, b] com uma certa tolerância 'tol'.
    """
    global tol
    a,b=encontrar_intervalo(f,A, B_min, B_max)

    # Loop principal de bisseção
    while True:
        m = (a + b) / 2  # ponto médio
        if abs(f(A,m)) < tol or abs(b - a) / 2 < tol:
            return m  # retorna a raiz aproximada

        # Verifica em qual metade está a raiz
        if f(A,a) * f(A,m) < 0:
            b = m  # raiz está no intervalo [a, m]
        else:
            # print(m)
            a = m  # raiz está no intervalo [m, b]



# Lista de valores de A, tal que A=k*pi e k pertence aos inteiros
As = [pi,2*pi,3*pi]
listaAB = []
# Valores inicialmente escolhidos para a e b
B_min1, B_max1 = -2*pi,-pi
B_min2,B_max2 = -pi+0.00001,0.0001
# Para cada valor de A, procurar as raízes de B
for A in As:
    #Cálculo dos valores de B
    B1 = bisseccao(f1,A, B_min1, B_max1)
    B2 = bisseccao(f1,A, B_min2, B_max2)
    B3 = bisseccao(f2,A, B_min1, B_max1)
    B4 = bisseccao(f2,A, B_min2, B_max2)
    
    #Conferindo se A e B são válidos e os adicionando a uma lista
    for B in [B1, B2,B3,B4]:
        if math.sin(B) !=0 and math.sin(3*B/2)!=0 and math.sin(A/2)!=0 and math.sin(3*A/2)!=0:
            listaAB.append([A,B])
    

def lista_AB_uv_xuvyuv(listaAB):

    #Iniciando a string que armazenará os resultados
    str='' 
    for AB in listaAB:
        A = AB[0]
        B = AB[1]

        #Cálculo de u e v
        u = (A + B) / 2
        v = (A-B)/2  
        
        # Cálculo de x e y com base na equação da curva estudada
        xu = 6 * math.cos(u) - 7 * math.cos(3 * u)
        yu = 6 * math.sin(u) - 7 * math.sin(3 * u)
        xv = 6 * math.cos(v) - 7 * math.cos(3 * v)
        yv = 6 * math.sin(v) - 7 * math.sin(3 * v)

        #filtrando valores não válidos pra u e v
        bate=(abs(xu-xv)<0.00001 and abs(yu-yv)<0.00001)
        if 0<=u<2*pi and 0<=v<2*pi and bate:
            str+=(f'A:{A:.4f}, B:{B:.4f} || u:{u:.4f}, v:{v:.4f},|| xu:{xu:.4f}, xv:{xv:.4f}|, yu:{yu:.4f}, yv:{yv:.4f}, ||bate:{bate} \n')
    return str
print(lista_AB_uv_xuvyuv(listaAB))