from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNOS: IAN ANTHONY SENA DA SILVA E JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA V - QUESTÃO 1


#Dados da questão
diametro = 0.15                    #Diâmetro do projétil (m)
densidade = 7800                   #Densidade do projétil (kg/m³)
cd = 0.47                          #Coeficiente aerodinâmico
angulo = radians(60)               #Valor do ângulo já convertido para radianos
velocidade = 300                   #Modulo da velocidade (m/s)


#Força de arrasto e Aceleração gravitacional

#Dados fornecidos pela questão
d_ar =  1.29                        #Densidade do ar (kg/m³)
lamb = 10000                        #Lambda (m)
r_terra = 6370 * 1000               #Raio da terra (m)
m_terra = 5.98 * 10 ** 24           #Massa da terra (kg)

#Dados necessários
h = 0                               #Altura inicial (m)
h_max = 0                           #Iniciando a altura ser máxima (m)
volume = 4/3 * pi * (diametro/2)**3 #Volume do projétil (m³)
massa = volume * densidade          #Massa do projétil (kg)
area = pi * (diametro/2)**2         #Área da superfície do projetil (m²)
coef = 1/2 * d_ar * area * cd       #Coeficiente do arrasto quadrático
k = 6.67408 * 10 **(-11)            #Constante gravitacional

#Caso real
p_real = vec(0,0,0)                 #Posição do projétil
g_real = (k * m_terra) / (r_terra + p_real.y)**2
a_real = vec(0,0,0)                   
grav_real = vec(0,-g_real,0)
v_real = vec(velocidade * cos(angulo), velocidade * sin(angulo), 0)

#Caso ideal
p_ideal = vec(0,0,0)                #Posição do projétil
g_ideal = (k * m_terra) / (r_terra)**2
a_ideal = vec(0,0,0)
grav_ideal = vec(0,-g_ideal,0) 
v_ideal = vec(velocidade * cos(angulo) , velocidade * sin(angulo) , 0)

#Gráfico
graph(title="Trajetória dos projéteis \n", xtitle="Alcance (m)", ytitle="Altura (m)", fast = False)
real = gcurve(color=vec(0.697, 0.435, 1.000), label="Real")
ideal = gcurve(color=vec(0.000, 0.435, 1.000), label="Ideal")


t = 0                           #Tempo inicial
dt = 0.001                      #Incremento de tempo


#Movimento do projétil para o caso real

while p_real.y >= 0:
    
    rate(10000)
    a_real = grav_real - (coef/massa) * (mag2(v_real) * hat(v_real)) * exp(-p_real.y / lamb) #Fórmula oferecida na questão
    v_real += a_real * dt
    p_real += v_real * dt
    
    t += dt
    real.plot(p_real.x, p_real.y) 
    
    
    if p_real.y > h_max:
        h_max = p_real.y
        

print(f"Para o caso real, temos: \n\nAlcance horizontal: {p_real.x: .3f} m.\nTempo de vôo: {t: .3f} s. \nAltura máxima: {h_max: .3f} m.")


#Movimento do projétil para o caso ideal
while p_ideal.y >= 0:
    rate(10000)
    
    a_ideal = grav_ideal - (coef/massa) * (mag2(v_ideal) * hat(v_ideal))
    
    v_ideal += a_ideal * dt
    p_ideal += v_ideal * dt
    ideal.plot(p_ideal.x, p_ideal.y)
    
    
    t += dt