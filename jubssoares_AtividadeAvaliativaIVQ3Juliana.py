from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA IV - QUESTÃO 3

#Dados da questão
m_maior = 45.4      #Massa da bola maior
m_menor = 0.454     #Massa da bola menor
h = 183             #Altura de lançamento das bolas
d_ferro = 7870      #Densidade do ferro
d_ar = 1.22         #Densidade do ar
cd = 0.47           #Coeficiênte aerodinâmico

#Dados necessários
v_maior = 0        #Velocidade inicial da bola maior
v_menor = 0        #Velocidade inicial da bola menor
a_maior = 0        #Aceleração inicial da bola maior
a_menor = 0        #Aceleração inicial da bola menor
g = -9.8           #Aceleração da gravidade
t = 0              #Tempo inicial
dt = 0.001         #Passo

#Cálculo dos diâmetros
dm_maior = ((6 * m_maior) * (pi/ d_ferro))**(1/3)
dm_menor = ((6 * m_menor) * (pi/ d_ferro))**(1/3)

#Calculando os raios
r_maior = dm_maior / 2
r_menor = dm_menor / 2

#Áreas
a_maior =  pi * r_maior**2
a_menor =  pi * r_menor**2

#Coeficiênte de arrasto quadrático
coef_maior = 0.5 * d_ar * a_maior * cd
coef_menor = 0.5 * d_ar * a_menor * cd

#Objetos
maior = sphere(pos = vec(0, h, 0), radius = r_maior * 30 , color = vec(0.734, 0.000, 0.872))
menor = sphere(pos = vec(15, h, 0), radius = r_menor * 30, color = vec(0.543, 0.619, 1.000))
piso = box(pos = vec(0, -7, 0), size = vec(150, 1, 20), color = vec(0.497, 0.634, 0.403))

#Ajustando a cena
scene.center = vec(r_maior, h/2, 0)
scene.height = 500
scene.width = 400
scene.fov = pi/4
scene.pause()

#Simulação
while maior.pos.y >= 0:
    rate(1000)
    
    af_maior = g + (coef_maior / m_maior) * v_maior ** 2
    v_maior += af_maior * dt
    maior.pos.y += v_maior * dt
    
    af_menor = g + (coef_menor / m_menor) * v_menor ** 2
    v_menor += af_menor * dt
    menor.pos.y += v_menor * dt
    
    t += dt
    
    
    
    #Determinação de qual esfera tocou primeiro no piso
    
    if maior.pos.y <= 0 or menor.pos.y <= 0:   
        if maior.pos.y > menor.pos.y:
            esfera = "menor"
            
        else:
            esfera = "maior" 
        break


    distancia = maior.pos.y - menor.pos.y
    
#Print com todas as informações    
print(f"A primeira massa a chegar no piso foi a {esfera}, com distância de {distancia: .3f} metros entre as massas, portanto, Galileu estava errado.")