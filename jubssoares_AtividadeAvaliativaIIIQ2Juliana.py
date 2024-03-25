from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA III - QUESTÃO 2


#Ajustando a cena
scene.width = 800
scene.height = 400
scene.center = vector(8,5,-1)
scene.pause()

#Carrinho 1
carro1 = box(pos = vec(0, 0, -1), size = vec(2.0, 0.4, 1.0), color = color.red, opacity = 0.7)

#Rodinhas
roda1 = cylinder(pos = vec(-0.5, -0.2, -0.5), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)
roda2 = cylinder(pos = vec(-0.5, -0.2, -1.7), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)
roda3 = cylinder(pos = vec(0.5, -0.2, -1.7), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)
roda4 = cylinder(pos = vec(0.5, -0.2, -0.5), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)

#Compondo o carrinho 1
carrinho1 = compound([carro1, roda1, roda2, roda3, roda4])

#Carrinho2
carro2 = box(pos = vec(0, 0, 1), size = vec(2.0, 0.4, 1.0), color = color.green, opacity = 0.7)

#Rodinhas
roda5 = cylinder(pos = vec(-0.5, -0.2, 0.3), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)
roda6 = cylinder(pos = vec(-0.5, -0.2, 1.5), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)
roda7 = cylinder(pos = vec(0.5, -0.2, 0.3), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)
roda8 = cylinder(pos = vec(0.5, -0.2, 1.5), radius = 0.2, axis = vec(0, 0, 1), length = 0.2)

#Compondo o carrinho 2
carrinho2 = compound([carro2, roda5, roda6, roda7, roda8])

#Pista
pista = box(pos = vec(8, -0.5 ,0), size = vec(25, 0.2, 6), color = color.white, texture = "https://t3.ftcdn.net/jpg/02/95/32/58/360_F_295325870_p2zO53PLWLqjuU4gbSm8usViHGB25Lyl.jpg")

#Variáveis para o carrinho 1
v1 = 2
a1 = 0.5

#Variáveis para o carrinho 2
v2 = 1
a2 = 1

#Váriaveis gerais

tempo = 0
dt = 0.01

#Gráfico da posição
graph(title="<b>Gráfico da posição.</b>", xtitle="t(s)", fast = False)
posicao1 = gcurve(color=color.red, width = 1.5 , label = "Posição: Carro vermelho")
posicao2 = gcurve(color=color.green, width = 1.5 , label = "Posição: Carro verde")

#Gráfico da velocidade
graph(title="<b>Gráfico da velocidade.</b>", xtitle="t(s)", fast = False)
velocidade1 = gcurve(color=color.red, width = 1.5 , label = "Velocidade: Carro vermelho")
velocidade2 = gcurve(color=color.green, width = 1.5 , label = "Velocidade: Carro verde")

#Gráfico da aceleração
graph(title="<b>Gráfico da aceleração.</b>", xtitle="t(s)", fast = False)
aceleracao1 = gcurve(color=color.red, width = 1.5 , label = "Aceleração: Carro vermelho")
aceleracao2 = gcurve(color=color.green, width = 1.5 , label = "Aceleração: Carro verde")

#Animação
while tempo < 5:
    rate(4/dt)
    v1 += a1 * dt
    v2 += a2 * dt
    carrinho1.pos.x += v1 * dt
    carrinho2.pos.x += v2 * dt
    tempo += dt
    
    velocidade1.plot(tempo,v1)
    velocidade2.plot(tempo,v2)
    posicao1.plot(tempo, carrinho1.pos.x)
    posicao2.plot(tempo, carrinho2.pos.x)
    aceleracao1.plot(tempo, a1)
    aceleracao2.plot(tempo, a2)
    
    x1 = carrinho1.pos.x
    x2 = carrinho2.pos.x
    dx = abs(x2) - abs(x1)
        
    
    if  0.0001 >= dx >= -0.0001 :
        tf = round(tempo)
        xf = round((x1 + x2) / 2,3)
        print(f" O tempo de encontro foi: {tf} s.")
        print(f" A posição de encontro foi: {xf} m.")
