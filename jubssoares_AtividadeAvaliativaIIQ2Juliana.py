from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA II - QUESTÃO 2

#Dados da questão

t = 0
g = -9.81 #m/s²
h = 8 #m
dt = 0.01
epsilon = 0.8 #coeficiente de restituição
epsilon2 = 0.785 #coeficiente de restituição
vx1 = 1.14 #velocidade da partícula no eixo x
vy1 = 0 #velocidade da partícula no eixo y
vx2 = 1.2 #velocidade da partícula no eixo x
vy2 = 0 #velocidade da partícula no eixo y
atrito = 0.05


#Simulação do movimento

plano = box(pos = vec(0, -5, 0), size = vec(40, 0.5, 5), color = vec(0.678, 0.705, 0.705))
p1 = sphere(radius = 0.45, color = vec(0.652, 0.000, 0.753), make_trail = True)
p2 = sphere(radius = 0.45, color = vec(0.526, 0.576, 1.000), make_trail = True)

#Posições das particulas no eixo y 

p1.pos.y = (plano.pos.y + plano.size.y/2 + p1.radius) + h
p2.pos.y = (plano.pos.y + plano.size.y/2 + p2.radius) + h

#Posição da particula 2 no eixo z
p2.pos.z = -2

#Deinição do loop para movimento

while t < 15 :
    rate(200)
    
    #Particula 1
    if p1.pos.y < -4.5:          # Se a esfera tocar no eixo y
        vy1 = -vy1 * epsilon         # velocidade de afastamento
        p1.pos.y = -4.5         
        vx1 = (1 - atrito) * vx1  # velocidade com o atrito
        
    p1.pos.y += vy1 * dt       
    p1.pos.x += vx1 * dt
    vy1 += g * dt
    
    #Partícula 2
    if p2.pos.y < -4.5:          # Se a esfera tocar no eixo y
        vy2 = -vy2 * epsilon2         # velocidade de afastamento
        p2.pos.y = -4.5          
        
        
    p2.pos.y += vy2 * dt 
    p2.pos.x += vx2 * dt
    vy2 += g * dt
    t += dt