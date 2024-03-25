from vpython import *
#Web VPython 3.2


''' 
QUESTAO 05 - AULA  12

1. Simule o movimento de um asteroide que se aproxima de um sistema binário. Adote s. Em caso de colisão o programa deverá parar e mostrar uma mensagem.
Dados:
Estrela 1:
• Posição inicial: (−5e11, 0, 0) m
• Massa: 3e30  kg
• Velocidade inicial: (0, 3e3, 0) m/s
Cometa:
• Posição inicial: (1.5e12, 0, 0) m
• Massa: 1e4 kg
• Velocidade inicial: (0, − 7.4e3, 0) m/s
Estrela 2:
• Posição inicial:(5e11, 0, 0) m
• Massa: 1.65e30 kg
• Velocidade inicial: (0, − 5.45e3, 0) m/s

2. Ainda considerando o programa desenvolvido no item 1 desta questão, realize as alterações nas condições iniciais do cometa sugeridas abaixo e descreva o seu
comportamento a curto e longo prazo. 
Condição 1:
• Posição inicial: (1.501e12, 0, 0) m
• Velocidade inicial: (0, − 7.4e3, 0) m/s
Condição 2:
• Posição inicial: (1.5e12, 0, 0) m
• Velocidade inicial: (0, − 7.4001e3, 0) m/s

'''

G = 6.7e-11                     #Constante

#OBJETOS E DADOS DO PROBLEMA
e1 = sphere(pos=vec(-5e11,0,0), radius = 3e10, color = color.yellow, make_trail = True, interval = 10)      #estrela 1
me1 = 3e30                      #massa em kg
ve1 = vec(0,3e3,0)              #velocidade em m/s
pe1 = me1 * ve1                 #momentum

e2 = sphere(pos=vec(5e11,0,0), radius = 2e10, color = color.red, make_trail = True, interval = 10)          #estrela 2
me2 = 1.65e30                   #massa em kg
ve2 = vec(0,-5.45e3,0)          #velocidade em m/s
pe2 = me2 * ve2                 #momentum

#Condição inicial do cometa
com = sphere(pos=vec(1.5e12, 0, 0), radius = 1.5e10, mass = 1e4, color = color.green, make_trail = True, interval = 10)     #cometa/asteroide
mcom = 1e4                      #massa em kg
vcom = vec(0, -7.4001e3, 0)     #velocidade em m/s
pcom = mcom * vcom              #momentum

#AJUSTE DE CENA
scene.title = "<h1>O problema dos três corpos</h1>"
scene.range= 1e12
scene.width = 800
scene.height = 500
scene.center=e2.pos
scene.zoom = True
scene.autoscale = True
scene.background = vec(0.000, 0.124, 0.310)
scene.fov = radians(5)
scene.pause()
dt = 1e5

#Animação
while True:
    rate(2000)
    
    #sistema binário entre as duas estrelas
    r12 = e2.pos - e1.pos
    F12 = G * me1 * me2/mag2(r12) * hat(r12)
    
    pe1 += F12 *dt
    e1.pos += pe1 / me1 * dt
    
    pe2 += - F12 *dt
    e2.pos += pe2 / me2 * dt
    
    #inclusão do asteróide/cometa interagindo com as estrelas
    r13 = com.pos - e1.pos
    r23 = com.pos - e2.pos
    
    #cálculo das forcas gravitacionais do cometa com cada estrela e forca resultante
    F32 = -G * mcom * me2/(mag2(r23)) * hat(r23)    #Força entre cometa e estrela 2
    F31 = -G * me1 * mcom/(mag2(r13)) * hat(r13)    #Força entre cometa e estrela 1
    F3 = F32 + F31                                  #Força total entre cometa e estrelas 1 e 2
    
    a3 = F3/mcom                #Aceleração
    vcom += a3 * dt             #atualização da velocidade
    com.pos += vcom * dt        #atualização da posição do cometa
    
        
    #Condição de parada caso tenha colisão entre as estrelas e o cometa.
    if mag(r13) <= (e1.radius + com.radius): 
        print("Houve colisão com a Estrela 1.")
        break
    if mag(r23) <= (e2.radius + com.radius): 
        print("Houve colisão com a Estrela 2.")
        break
    
    
    #Condição para alterar dt. A ideia básica é que quando o asteróide chega muito perto de qualquer uma das estrela o movimento não fica suave,
    #então precisamos calcular com mais precisão, reduzindo o dt. aqui o asteróide ganha muita velocidade e cobre muito espaço entre passsos de tempo sucessivos, por isso devemos ajustar o dt.
    elif mag(r13) < 1.5 * e1.radius:
        dt = 1e-6
    elif mag(r23) < 1.5 * e2.radius:
        dt = 1e-6
    else: dt = 1e5
    
    
    
   





