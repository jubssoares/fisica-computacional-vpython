from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA IV - QUESTÃO 4


#Dados do programa
d_ar = 1.3               #Densidade do ar
vis_ar = 1.8             #Viscosidade do ar
g = vector(0, -9.8, 0)   #Aceleração devido à gravidade
raio = 0.15              #Raio da esfera (diamentro = 30 cm)
massa = 3.0              #Massa da esfera
h = 100.0                #Altura inicial (m)
cd = 0.74                #Coeficiente de arrasto
d = 0.30                 #Diametro

#Área de seção transversal
area = pi * raio**2

#Objetosw
esfera = sphere(radius=raio * 50 , color = vec(1.000, 0.674, 0.872))
solo = box(pos = vec(0, -raio * 50, 0), size = vec(100, 1, 20), color = color.green)

#Ajustando a cena
scene.center = vec(raio, h/2, 0)
scene.width = 400
scene.legth = 400
scene.pause()

#Posiciona a esfera na altura inicial
esfera.pos = vec(0, h, 0)

#Inicializa a velocidade
velocidade = vec(0, 0, 0)

#Inicializa o tempo
tempo = 0

#Simulação
dt = 0.01  # Intervalo de tempo
while esfera.pos.y >= 0:
    rate(100)  # Taxa de atualização
    # Calcula a força do arrasto
    arrasto = -0.5 * d_ar * cd * area * mag(velocidade) * velocidade
    # Calcula a força peso
    peso = massa * g
    # Calcula a aceleração
    aceleracao = (peso + arrasto) / massa
    # Atualiza a velocidade
    velocidade += aceleracao * dt
    # Atualiza a posição
    esfera.pos += velocidade * dt
    # Atualiza o tempo
    tempo += dt

#Descobrindo o tipo de arrasto
peso = massa * g
coef_a_l = 3 *  pi * vis_ar            #Coeficiente de arrasto linear
coef_a_q = 0.5 * d_ar * area * cd      #Coeficiente de arrasto quadrático
vl_l = massa * 9.8 / coef_a_l                #Velocidade limite no arrasto linear
vl_q = sqrt( peso / coef_a_q)          #Velocidade limite no arrasto quadrático
cte_b = 6 * pi * raio * vis_ar         #Coeficiente b na formula do arrasto linear = -bv
prandtl = 0.5 * d_ar * area * cd       #Número de prandtl


arrasto_l = cte_b * vl_l               #Arrasto linear
arrasto_q = prandtl * vl_q             #Arrasto quadrático


rn_l = (d_ar * d * vl_l) / vis_ar      #Número de reynolds para o arrasto linear
rn_q = (d_ar * d * vl_q) / vis_ar      #Número de reynolds para o arrasto quadrático

arrasto = 0                            #Variável do arrasto "vazia"
tipo = ""                              #Variável do tipo "vazia"
coef = 0                               #Variável vazia do coeficiente

if rn_q/rn_l >= 100:               
                                      
    arrasto = arrasto_q                 
    tipo = "Arrasto quadrático"   
    coef = coef_a_q
    
else:
    arrasto = arrasto_l
    tipo = "Arrasto linear"
    coef = coef_a_l

#Gráficos da posição, velocidade e aceleração em função do tempo
graph_posicao = graph(title=tipo, xtitle="Tempo (s)", fast = False)
posicao_t = gcurve(color = vec(0.075, 0.366, 0.513), label = "y(t)")
velocidade_t = gcurve(color = vec(1.000, 0.315, 0.302), label = "v(t)")
aceleracao_t = gcurve(color = vec(0.258, 0.788, 0.514), label = "a(t)")

#Resetando as variáveis para plotagem
tempo = 0
esfera.pos = vector(0, h, 0)
velocidade = vector(0, 0, 0)

while esfera.pos.y >= 0:
    rate(100)
    arrasto = -0.5 * d_ar * cd * area * mag(velocidade) * velocidade
    peso = massa * g
    aceleracao = (peso + arrasto) / massa
    esfera.pos += velocidade * dt
    velocidade += aceleracao * dt
    tempo += dt

    posicao_t.plot(tempo, esfera.pos.y)
    velocidade_t.plot(tempo, velocidade.y)
    aceleracao_t.plot(tempo, aceleracao.y)

#Tipo de arrasto
print(f"O tipo de arrasto é o {tipo}.")

#Quanto tempo levará para atingir 98% da velocidade limite
vl = sqrt(massa * -9.8 / (0.5 * d_ar * cd * area))
vl_98 = 0.98 * vl
print(f"Tempo para atingir 98% da velocidade limite: {vl_98} segundos.")

# Quanto tempo levará para chegar ao solo
print(f"Tempo para atingir o solo: {tempo: .3f} segundos.")