from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA IV - QUESTÃO 1

#Dado solicitados ao usuário
vo = float(input("Insira um valor para a velocidade inicial (V0): "))
d =  float(input("Insira um valor para a distância inicial (D): "))
h =  float(input("Insira um valor para a altura inicial (H): "))

#Criando os objetos
macaco = sphere(pos = vec( 0 + d, h, 0), radius = 0.5, color = vec(0.736, 0.513, 0.374), make_trail= True)
dardo = sphere(pos = vec(0,0,0), radius = 0.1, color=color.red, make_trail = True)
chao = box(pos=vec(0, -0.5 - dardo.radius, 0), size=vec(d * 2.5, 1, 0.5), color=color.green)

#Dados do programa 
angulo = atan(h/d)                    #Ângulo entre o índio e o macaco
voydardo =   vo * sin(angulo)         #Velocidade eixo y dardo
voymacaco =   0                       #Velocidade eixo y macaco
vox = vo * cos(angulo)                #Velocidade eixo x
ay = 9.8                              #Aceleração eixo y
ax = 0                                #Aceleração eixo x
dt = 0.001                            #Passo
t = 0                                 #Tempo inicial

#Ajuste da cena
scene.pause()
scene.center = vec(d / 2 , h , -10)

#Looping
while dardo.pos.y >= 0 and macaco.pos.y  >= 0:
    rate(1/dt)
    
    voydardo -= ay * dt                  #Movimento pelo método de euler-cromer    
    dardo.pos.y += voydardo * dt
    dardo.pos.x += vox * dt
    
    voymacaco -= ay * dt
    macaco.pos.y += voymacaco * dt
    
    
    t += dt 

#Caso o dardo atinja o macaco
    if  mag(dardo.pos - macaco.pos) <= (dardo.radius + macaco.radius) :
        print(f"O tempo para o macaco ser atingido foi: {t:.3f} s. ")
        print(f"A velocidade inicial mínima necessária para que o macaco seja atingido é dada pela expressão V0 = D / cos(theta) * sqrt(2H /g).")
        print(f"A posição de encontro foi: {macaco.pos.y:.3f} m de altura e a {dardo.pos.x:.3f} m da posição inicial do índio.")
        break