
import math
import numpy as np

def distancia_euclidiana(x, y):
    """
    Calcula a distância euclidiana entre dois pontos (p1 e p2) no plano cartesiano
    """
    return math.sqrt((x) ** 2 + (y) ** 2)
def funcx(t):
    """
    com base na equação da curva dada, calcula o valor de x para certo parâmetro (t)
    """
    return 6 * math.cos(t) - 7 * math.cos(3 * t)

def funcy(t):
    """
    com base na equação da curva dada, calcula o valor de y para certo parâmetro (t)
    """
    return 6 * math.sin(t) - 7 * math.sin(3 * t)


def a(k):
    A = k*math.pi
    return A

def acha_ABs(delta_B, margemB,margem_dif_uv):
    #u pertence a [0, 2pi[
    #v pertence a [0, 2pi[
    #A = u + v
    #A pertence a [0, 4pi[
    As_e_Bs = []

    for k in range (1,3):
        A = a(k)
        

        #u pertence a [0, 2pi[
        #v pertence a [0, 2pi[
        #B = u -v
        #B pertence a ]-2pi, 2pi[

        for B in np.arange(-2*math.pi,delta_B):
            if abs(6*math.cos(A/2)*math.sin(B/2)-7*math.sin(3*A/2)*math.sin(3*B/2))<margemB:
                As_e_Bs.append([A,B])
            
    return As_e_Bs

def acha_uv_xy(delta_B, margemB, margem_dif_uv):
    As_e_Bs = acha_ABs(delta_B, margemB, margem_dif_uv)
    uv_xys=[]

    for A_e_B in As_e_Bs:
        
        A=A_e_B[0]
        B=A_e_B[1]
        # u-v=B
        # u+v=A

        # 2u=B+A
        # u=(B+A)/2

        # v = A-u

        u=(A+B)/2
        v = A-u
        
        if abs(B)>margem_dif_uv:
            x=funcx(u)
            y=funcy(u)

            
            uv_xys.append([[u,v],[x,y]])
    return uv_xys

def filtra_t_x_e_y_proximos(delta_B, margemB, margem_ponto, margem_dif_uv):
    """
    Tira pontos que estão próximos entre si e retorna uma lista filtrada a partir do uso da distância euclidiana desses pontos entre si.
    """
    # acha as coordenadas a serem filtradas
    pontos = acha_uv_xy(delta_B, margemB, margem_dif_uv)  #[[u,v],[x,y]]
    
    # lista que vai armazenar os pontos filtrados
    pontos_filtrados = []

    # itera sobre todos os pontos obtidos
    for ponto in pontos:
        # Extrai as coordenadas x e y do ponto
        x = ponto[1][0]
        y = ponto[1][1]
                
        ponto_proximo = False  # marca se o ponto é próximo de algum ponto já filtrado

        for p in pontos_filtrados:  # itera pelos pontos filtrados
            distancia = distancia_euclidiana(x - p[1][0], y - p[1][1])
            if distancia < margem_ponto:  # Calcula a distância euclidiana entre o ponto atual e um ponto já filtrado e se a
                # distância for menor ou igual à distância mínima, o ponto é marcado como próximo e o ciclo é interrompido
                ponto_proximo = True
                break

        # Se o ponto não estiver próximo de nenhum dos outros pontos filtrados, esse ponto é salvo
        if not ponto_proximo:
            pontos_filtrados.append(ponto)

    # Retorna a lista de pontos filtrados
    return pontos_filtrados

def formata(delta_B, margemB, margem_ponto, margem_dif_uv):
    """
    Formata o que vai aparecer no terminal, de acordo com o formato pedido (txy ou xy), sendo que txy mostra os tês e xy, não.
    """
    lista = filtra_t_x_e_y_proximos(delta_B, margemB, margem_ponto, margem_dif_uv) #pega todos os pontos de interseção já filtrados #[[u,v],[x,y]]

    texto = f'len = {len(lista)}\n\n'  # inicia a string de retorno, com o número de pontos achados
    
    # Formata a saída 
    for item in lista:
        u = item[0][0]
        v = item[0][1]
        x = item[1][0]
        y = item[1][1]
        if x<0:  #ajuste para alinhar o texto
            texto += f'u:{u:.3f}, v:{v:.3f} || x:{x:.3f} | y:{y:.3f} \n'
        else:
            texto += f'u:{u:.3f}, v:{v:.3f} || x:{x:.3f}  | y:{y:.3f} \n'

    return texto

delta_B = 0.001
margemB = 0.1
margem_ponto = 4
margem_dif_uv = 0.1
print(formata(delta_B, margemB, margem_ponto, margem_dif_uv))

            

        
