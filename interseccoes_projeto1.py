import math

# Funções principais de cálculo

def funcx(t):
    """
    com base na equação da curva dada, calcula o valor de x para certo parâmetro t
    """
    return 6 * math.cos(t) - 7 * math.cos(3 * t)

def funcy(t):
    """
    com base na equação da curva dada, calcula o valor de y para certo parâmetro t
    """
    return 6 * math.sin(t) - 7 * math.sin(3 * t)

def distancia_euclidiana(p1, p2):
    """
    Calcula a distância euclidiana entre dois pontos (p1 e p2) no plano cartesiano
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

###### Funções que utilizam os valores de funcx e funcy para encontrar encontros e da distancia_euclidiana, para os filtrar

def acha_ts_e_coordenadas(difmin, delta, t10, t20):
    """
    Esse método numérico consiste em iterar pelo conjunto de tês possíveis (que ocorrem entre certo t10 e t20 previamente definidos) e os aplicar na 
    equação da curva; as iterações consistem em, inicialmente, os valores do x1 e x2 serem calculados com base em dois tês diferentes, o valor deles, 
    então, é comparado a partir de uma subtração. Se o resultado dessa subtração possuir um módulo inferior a um valor predefinido (difmin), o mesmo 
    acontecerá para y1 e y2. Caso sejam suficientemente próximos entre si, o valor dos tês e de um dos xs (x1) e um dos ys (y1) é armazenado em uma lista.
    """
    t_de_encontros = []  # Lista para armazenar os encontros
    t1 = t10

    # Loop principal para t1
    while t1 < 2 * math.pi:
        t2 = t20  # Reiniciar t2 para cada t1
        while t2 >= 0:  # Assegurar que t2 não vai abaixo de 0
            #x1 e x2 são calculados a partir da equação da curva para o eixo x, representada, aqui, pela função funcx()
            x1 = funcx(t1) 
            x2 = funcx(t2)
            
            difx = x1 - x2 # Calcula as diferença entre x1, x2 
            if abs(difx) < difmin and abs(t1 - t2) > 0.1: #não deixa os ts serem iguais e checa pra ver se o x1 e x2 são iguais
                y1 = funcy(t1)  
                y2 = funcy(t2)
                dify = y1 - y2  #calcula a diferença entre y1 e y2

                if abs(dify) < difmin:   #checa pra ver se o y1 e y2 são iguais
                    t_de_encontros.append([[t1, t2], [x1, y1]]) #coloca na lista os tês e a coordenada
            t2 -= delta  # reduz t2

        t1 += delta  # aumenta t1

    return t_de_encontros


#################### a partir daqui, ocorrerá a filtragem e formatação dos resultados

##############filtragem dos pontos
def filtra_t_x_e_y_proximos(difmin, delta, t10, t20, distancia_minima):
    """
    Tira pontos que estão próximos entre si e retorna uma lista filtrada a partir do uso da distância euclidiana desses pontos entre si.
    """
    # acha as coordenadas a serem filtradas
    pontos = acha_ts_e_coordenadas(difmin, delta, t10, t20)
    
    # lista que vai armazenar os pontos filtrados
    pontos_filtrados = []

    # itera sobre todos os pontos obtidos
    for ponto in pontos:
        # Extrai as coordenadas x e y do ponto
        x, y = ponto[1]
                
        ponto_proximo = False  # marca se o ponto é próximo de algum ponto já filtrado

        for p in pontos_filtrados:  # itera pelos pontos filtrados
            if distancia_euclidiana([x, y], [p[1][0], p[1][1]]) < distancia_minima:  # Calcula a distância euclidiana entre o ponto atual e um ponto já filtrado e se a
                # distância for menor ou igual à distância mínima, o ponto é marcado como próximo e o ciclo é interrompido
                ponto_proximo = True
                break

        # Se o ponto não estiver próximo de nenhum dos outros pontos filtrados, esse ponto é salvo
        if not ponto_proximo:
            pontos_filtrados.append(ponto)

    # Retorna a lista de pontos filtrados
    return pontos_filtrados



############## Função final para formatar os resultados

def formata(difmin, delta, t10, t20, formato, distancia_minima):
    """
    Formata o que vai aparecer no terminal, de acordo com o formato pedido (txy ou xy), sendo que txy mostra os tês e xy, não.
    """
    lista = filtra_t_x_e_y_proximos(difmin, delta, t10, t20, distancia_minima) #pega todos os pontos de interseção já filtrados
    
    # inicia a string de retorno, com o número de pontos achados
    texto = f'len = {len(lista)}\n\n'
    
    # Formata a saída de acordo com o formato especificado (txy ou apenas xy)
    for item in lista:
        if formato == 'txy':
            t1 = item[0][0]
            t2 = item[0][1]
            x = item[1][0]
            y = item[1][1]
            if x<0:  #ajuste para alinhar o texto
                texto += f't1:{t1:.3f}, t2:{t2:.3f} || x:{x:.3f} | y:{y:.3f} \n'
            else:
                texto += f't1:{t1:.3f}, t2:{t2:.3f} || x:{x:.3f}  | y:{y:.3f} \n'

        else:
            x = item[1][0]
            y = item[1][1]
            if x<0: #ajuste para alinhar o texto
                texto += f'x:{x:.3f} | y:{y:.3f} \n'
            else:
                texto += f'x:{x:.3f}  | y:{y:.3f} \n'

    return texto


# Parâmetros e execução
difmin = 0.001
delta = 0.001
x0 = 0
y0 = 2 * math.pi
formato = 'txy'
distancia_minima = 1

# Gera o texto formatado com os resultados
texto = formata(difmin, delta, x0, y0, formato, distancia_minima)

# Exibe o resultado
print(texto + "\n\n\n *Vale ressaltar que o ponto (-1, 0) não deve ser levado em conta, já que t1 e t2 são 2 pi e 0 nesse ponto. Graças à periodicidade das funções trigonométricas, com esses valores, representam o mesmo ponto, e portanto, não deve ser considerado um encontro distinto.")
