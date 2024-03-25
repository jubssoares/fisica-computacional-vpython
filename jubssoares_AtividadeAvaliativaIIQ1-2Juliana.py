from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA II - QUESTÃO 1

#Dados da questão

n = 3
v0 = 5 #m/s
h0 = 8 #m
g = 9.81 #m/s²
gy = -9.81 #m/s²
epsilon = 0.785 #coeficiente de restituição
dt = 0.001
t = 0

#Altura no terceiro salto:

expoente = 2 * n
hn = (h0 + ((v0 ** 2) / (2 * g))) * epsilon ** expoente
print(f"A altura máxima no 3° salto é: {hn: .2f} metros.")

#Simulação do movimento

plano = box(pos = vec(0, -5, 0), size = vec(15, 0.5, 5), color = vec(0.678, 0.705, 0.705))

particula = sphere(radius = 0.75, color = vec(0.652, 0.000, 0.753))

particula.pos.y = (plano.pos.y + plano.size.y/2 + particula.radius) + h0  #Posição da esfera no eixo y 

periodo =  sqrt(2 * h0 / abs(g))  #Periodo do movimento

#Deinição do loop para movimento
 
vy = -5

while t < 4 * periodo :
    rate(1000)
    if particula.pos.y < -4:          # Se a esfera tocar no eixo y
        vy = -vy * epsilon                 # velocidade de afastamento
        particula.pos.y = -4      
       
    particula.pos.y += vy * dt 
    vy += gy * dt
    t += dt



