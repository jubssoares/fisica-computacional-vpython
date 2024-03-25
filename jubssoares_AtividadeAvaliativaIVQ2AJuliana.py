from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA IV - QUESTÃO 2 - LETRA A

#Dados do programa

inclinacao = atan(0.2)       #Inclinação do terreno
direcao = radians(30)        #Direção de lançamento do projétil
v0 = 30                      #Velocidade de lançamento do projétil
g = vec(0, -9.8, 0)          #Vetor aceleração
t = 0                        #Tempo inicial
dt = 0.001                   #Passo
espessura = 1                #Espessura do terreno
raio = 0.5                   #Raio do projétil
comprimento = 100            #Comprimento do terreno


#Criando os objetos

projetil = sphere(pos = vec(raio, raio + espessura/2, 0), radius = raio, color = color.red, make_trail = True)
terreno = box(pos = vec(comprimento/2, (comprimento/2) * 0.22, 0), size = vec(comprimento, espessura, 5), axis = vec(cos(inclinacao), sin(inclinacao), 0), color = color.green)

#Ajustando a cena
scene.center = vec(comprimento/2, (comprimento/2) * 0.22, 0)
scene.pause()

#Loop
for i in arange(5,75,5):
    
    projetil = sphere(pos = vec(raio, raio + espessura/2, 0), radius = raio, color = color.red, make_trail = True)
    direcao = radians(i)
    v1 = vec(v0 * cos(inclinacao + direcao), v0 * sin(inclinacao + direcao), 0)
    
    
    while projetil.pos.y > 0:
        rate(2/dt)
        v1 += g * dt
        projetil.pos += v1 * dt
        t += dt
        dx = projetil.pos.x - projetil.radius
        dy = projetil.pos.y - (projetil.radius + 1/2) 
        angulo = dy/dx
        if angulo <= 0.2:   #Se o angulo entre a posição no eixo y e o eixo x for menos que 0,2, a esfera passou do plano.
            projetil = sphere(pos = vec(0.5, 0.5 + 1/2 ,  0), radius = 0.5, color = color.red, make_trail = True)
            break