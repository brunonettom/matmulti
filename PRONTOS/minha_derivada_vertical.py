import math
import numpy as np
pi = math.pi  # Define a constante pi

def df_dtx(t):  # Define a função f(t)
    resultado = -6 * math.sin(t) + 21 * math.sin(3 * t)
    return resultado

def df_dtx_linha(t):  # Define a derivada f'(t)
    resultado = -6 * math.cos(t) + 63 * math.cos(3 * t)
    return resultado

def ajustar_intervalo(t):  # Ajusta t para o intervalo [0, 2π)
    while t < 0:
        t += 2 * pi  # Se t for negativo, adiciona 2π até ficar positivo
    while t >= 2 * pi:
        t -= 2 * pi  # Se t for maior ou igual a 2π, subtrai 2π até ficar menor
    return t

def newton_method(t0, tol=1e-10):  # Método de Newton-Raphson
    t = t0
    while True:
        derivada_primeira = df_dtx(t)       # Calcula f(t) no ponto t
        derivada_segunda = df_dtx_linha(t)  # Calcula f'(t) no ponto t
        
        if derivada_segunda == 0:
            return None  # Evita divisão por zero
        
        t_novo = t - derivada_primeira / derivada_segunda  # Atualiza t
        
        if abs(t_novo - t) < tol:
            t_novo = ajustar_intervalo(t_novo)  # Ajusta t_novo para o intervalo [0, 2π)
            return t_novo  # Convergência atingida
        
        t = t_novo  # Prepara para a próxima iteração
    

def filtrar_valores_proximos(lst, limite):  # Filtra valores próximos em uma lista
    lst_ordenada = sorted(lst)  # Ordena a lista
    lst_filtrada = []
    ultimo_valor = None
    for valor in lst_ordenada:
        if ultimo_valor is None or abs(valor - ultimo_valor) > limite:
            lst_filtrada.append(valor)  # Adiciona se não for próximo do anterior
            ultimo_valor = valor  # Atualiza o último valor
    return lst_filtrada

def filtrar_pontos_proximos(pontos, limite):  # Filtra pontos (x, y, t) próximos
    pontos_filtrados = []
    for ponto in pontos:
        muito_proximo = False
        for pf in pontos_filtrados:
            distancia = math.hypot(ponto[0] - pf[0], ponto[1] - pf[1])  # Calcula a distância entre pontos
            if distancia < limite:
                muito_proximo = True  # Ponto é muito próximo de um já existente
                break
        if not muito_proximo:
            pontos_filtrados.append(ponto)  # Adiciona ponto único
    return pontos_filtrados

# Encontrar as raízes usando Newton-Raphson
ts = []
for t0 in np.linspace(0, 2 * pi, 1000):  # Chutes iniciais entre 0 e 2π
    t_real = newton_method(t0)  # Aplica o método de Newton-Raphson
    if t_real is not None and 0 <= t_real <= 2 * pi:
        ts.append(t_real)  # Adiciona raiz encontrada

# Remover valores duplicados nas raízes
limite_proximidade_t = 1e-6  # Limite para considerar valores próximos
ts_unicas = filtrar_valores_proximos(ts, limite_proximidade_t)

# Calcular os pontos (x, y) correspondentes às raízes
pontos = []
for raiz in ts_unicas:
    x = 6 * math.cos(raiz) - 7 * math.cos(3 * raiz)  # Calcula coordenada x
    y = 6 * math.sin(raiz) - 7 * math.sin(3 * raiz)  # Calcula coordenada y
    pontos.append((x, y, raiz))  # Adiciona o ponto e t à lista

# Filtrar pontos muito próximos
limite_proximidade_pontos = 1e-3  # Limite para considerar pontos próximos
pontos_filtrados = filtrar_pontos_proximos(pontos, limite_proximidade_pontos)

# Exibir os pontos filtrados com os valores de t
print(f"Número de pontos únicos encontrados: {len(pontos_filtrados)}")
str_pontos = ''
for ponto in pontos_filtrados:
    str_pontos += f"t = {ponto[2]:.3f} -> ({ponto[0]:.3f}, {ponto[1]:.3f})\n"  # Inclui t
print(str_pontos)
