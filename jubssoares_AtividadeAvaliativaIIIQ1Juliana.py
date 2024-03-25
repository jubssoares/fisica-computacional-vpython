from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA III - QUESTÃO 1


#Ajustando a cena
scene.pause()

#Valores adotados para a caixa
lado = 12.0
esp = 0.2
a = 2 * lado - esp
b = 2 * lado + esp

#Faces verticais
lado1 = box (pos=vector( lado, 0, 0), size=vector(esp, a, b),  color = color.green)
lado2 = box (pos=vector(-lado, 0, 0), size=vector(esp, a, b),  color = color.green)

#Faces horizontais
lado3 = box (pos=vector(0, -lado, 0), size=vector(b, esp, b),  color = color.blue)
lado4 = box (pos=vector(0,  lado, 0), size=vector(b, esp, b),  color = color.blue)

#Fundo
fundo = box(pos=vector(0, 0, -lado), size=vector(a, a, esp),   color = color.blue)

#Frente
frente = box(pos=vector(0, 0, +lado), size=vector(a, a, esp), opacity = 0)

#Dados da bolinha
bolinha = sphere (pos = vector(0, 0, 0), color = color.red, radius = 1.0)
bolinha.massa = 1.0
bolinha.v = vector (-0.15, -0.23, +0.27)

#Trajetória
trajetoria = curve(color = color.white)

#Gráfico da energia mecânica
graph(title="<b>Energia mecânica.</b>", xtitle="t(s)", fast = False)
emec = gcurve(label="Energia Mecânica", color=color.cyan)

#Gráfico da velocidade
graph(title="<b>Velocidade das componentes X e Y.</b>", xtitle="t(s)", fast = False)
velocidadex = gcurve(color=color.yellow, width = 1.5 , label = "Velocidade: X")
velocidadey = gcurve(color=color.orange, width = 1.5 , label = "Velocidade: Y")

#Incremento de tempo
dt = 0.5

#Reflexão ao quicar nas paredes
lado = lado - esp*0.5 - bolinha.radius

t = 0
tempo = 0
#Animação
while tempo < 10:
    rate(200)
    bolinha.pos = bolinha.pos + (bolinha.v/bolinha.massa)*dt
    
    if not (lado > bolinha.pos.x > -lado):
        bolinha.v.x = -bolinha.v.x
    if not (lado > bolinha.pos.y > -lado):
        bolinha.v.y = -bolinha.v.y
    if not (lado > bolinha.pos.z > -lado):
        bolinha.v.z = -bolinha.v.z
        
    trajetoria.append(pos=bolinha.pos)  
   
    
    #Energia Cinética
    Ec = 0.5 * bolinha.massa * bolinha.vel**2
    
    # Energia Potencial
    Ep = bolinha.massa * g * bolinha.pos.y

    # Energia Mecânica
    Em  = Ec + Ep

    #Plotando as curvas
    velocidadex.plot(t, bolinha.v.x)
    velocidadey.plot(t, bolinha.v.y)
    emec.plot(t, Em)
    
    
    g = 9.8
    bolinha.vel = 0
    
    #Euler-Cromer
    bolinha.vel += -g*dt
    #bolinha.pos.y += bolinha.vel * dt
    t += dt
    
    
    
    
