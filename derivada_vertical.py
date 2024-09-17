import math

t = 0
func = -6*math.sin(t) + 21*math.sin(3*t)
valores_t = []
while t <= 6.28:

    #PEGA O VALOR ATUAL DA FUNÇÃO
    func = -6*math.sin(t) + 21*math.sin(3*t)

    # VERIFICA SE O VALOR DA FUNÇÃO É APROXIMADAMENTE ZERO E COMPARA COM O PRÓXIMO VALOR PARA VER SE ELA É REALMENTE O MAIS PRÓXIMO DE ZERO
    if -0.05 < func < 0.05:
        mais_proximo = abs(func)
        proximo = abs(-6*math.sin(t+0.001) + 21*math.sin(3*(t+0.001)))
        if mais_proximo < proximo:
            valores_t.append(t)
    
    t += 0.001


for i in range(len(valores_t)):
    print(f'Valores da função: {(-6*math.sin(valores_t[i]) + 21*math.sin(3*valores_t[i])):.3f}, valores de t: {valores_t[i]:.3f}')
