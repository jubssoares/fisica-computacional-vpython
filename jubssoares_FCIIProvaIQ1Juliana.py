from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#PROVA 1 - QUESTÃO 1

#Dados da questão

d1 = 10
d2 = 25
periodo = 2.5
dt = 0.01
k = 1

#Ajustando a cena
scene.width = 600
scene.height = 600
scene.center = vec(0, 0, 0)
scene.range = 40


#Sistema solar
sol = sphere(pos=vec(0, 0, 0), radius = 2.0, color = color.yellow)
p1 = sphere(pos=vec(-d1, 0, 0), radius = 0.5, color = color.green, make_trail=True)
p2 = sphere(pos=vec(-d2, 0, 0), radius = 0.75, color = color.red, make_trail=True)

#Vetores velocidade e aceleração
v1 = arrow(pos=vec(-d1 + 0.5, 0, 0), length = 2.5, round = True, shaftwidth = 0.25, color = color.yellow)
a1 = arrow(pos=vec(-d1, 0, 0), axis=vec(0, -pi/2 - 0.5, 0), length = 2, round = True, shaftwidth = 0.25, color = color.white)
v2 = arrow(pos=vec(-d2 + 0.75, 0, 0), length = 2.5, round = True, shaftwidth = 0.25, color = color.yellow)
a2 = arrow(pos=vec(-d2, 0, 0), axis=vec(0, -pi/2 - 0.75, 0), length = 2.5, round = True, shaftwidth = 0.25, color = color.white)

#Objetos compostos dos planetas
planeta1 = compound([p1, v1, a1], make_trail = True)
planeta2 = compound([p2, v2, a2], make_trail = True)

#Movimento circular

#Dados Planeta 1
a1 = 10  # Amplitude
t = 0  # Tempo
omg = 2

#Dados Planeta 2
a2 = 30
omg2 = 0.38


#Animação
while t <= 2*periodo:
    rate(200)
    planeta1.pos.x = a1*cos(omg*t)
    planeta1.pos.y = a1*sin(omg*t)
    t += dt
    planeta2.pos.x = a2*cos(omg2*t)
    planeta2.pos.y = a2*sin(omg2*t)

    
    theta1 = atan(omg * t)
    theta2 = atan(omg2 * t)
    theta = theta1 + theta2

print(f"Distância angular entre os planetas =  {theta: .2f}°")
    