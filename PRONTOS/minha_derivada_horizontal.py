import math
import numpy as np
pi = math.pi  # Define a constante pi

def df_dty(t):  # Define a função f(t)
    return 6 * math.cos(t) - 21 * math.cos(3 * t)

def df_dty_linha(t):  # Define a derivada f'(t)
    return -6 * math.sin(t) + 63 * math.sin(3 * t)

def ajustar_intervalo(t):  # Ajusta t para o intervalo [0, 2π)
    return t % (2 * pi)

def newton_method(t0, tol=1e-10):  # Método de Newton-Raphson com limite de iterações
    t = t0
    while True:
        derivada_primeira = df_dty(t)       # Calcula f(t) no ponto t
        derivada_segunda = df_dty_linha(t)  # Calcula f'(t) no ponto t

        # Verifica se a derivada é muito pequena
        if abs(derivada_segunda) < 1e-8:
            return None  # Evita divisão por zero ou valores muito grandes

        t_novo = t - derivada_primeira / derivada_segunda  # Atualiza t

        if abs(t_novo - t) < tol:
            t_novo = ajustar_intervalo(t_novo)  # Ajusta t_novo para o intervalo [0, 2π)
            return t_novo  # Convergência atingida

        t = t_novo  # Prepara para a próxima iteração


def filtrar_valores_proximos(lst, limite):  # Filtra valores próximos em uma lista
    lst_filtrada = []
    for valor in sorted(lst):
        if not lst_filtrada or abs(valor - lst_filtrada[-1]) > limite:
            lst_filtrada.append(valor)
    return lst_filtrada

def filtrar_pontos_proximos(pontos, limite):  # Filtra pontos (x, y, t) próximos
    pontos_filtrados = []
    for ponto in pontos:
        if all(math.hypot(ponto[0] - pf[0], ponto[1] - pf[1]) > limite for pf in pontos_filtrados):
            pontos_filtrados.append(ponto)
    return pontos_filtrados

# Encontrar as raízes usando Newton-Raphson
ts = []
# Usar mais chutes iniciais para cobrir melhor o intervalo
chutes_iniciais = np.linspace(0, 2 * pi, 2000)
for t0 in chutes_iniciais:
    t_real = newton_method(t0)
    if t_real is not None and 0 <= t_real <= 2 * pi:
        ts.append(t_real)

# Remover valores duplicados nas raízes
limite_proximidade_t = 1e-5  # Ajuste do limite para considerar valores próximos
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
for ponto in pontos_filtrados:
    t_formatado = round(ponto[2], 6)
    x_formatado = round(ponto[0], 6)
    y_formatado = round(ponto[1], 6)
    print(f"t = {t_formatado:.6f} -> ({x_formatado:.6f}, {y_formatado:.6f})")
