from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA III - QUESTÃO 3


#Dados da questão
vx = 15
vy = 0
ax = 0
ay = -9.8
dt = 0.001
tempo = 0

#Valores adotados para os objetos
raio_a = 3.0
raio_c = 1.5
esp_asa = 0.5
tamanho_a = 8.0

#Compondo a cena

#Ajustes
#scene.width = 800
#scene.height = 500
scene.center = vec (0, 20, 0)
scene.pause()


#Objetos 
chao = box(pos = vec(0, -1, 0), size = vec(120, 0.5, 30), color = color.green, texture = "https://as1.ftcdn.net/v2/jpg/02/13/05/88/1000_F_213058852_gcyHL0rf0iY7Pe6fustm1eKRFm7qek5A.jpg")

fuselagem = cylinder(pos = vec(-60 - (tamanho_a/2), 40 + (raio_a/2), 0), radius = raio_a, length = 10, axis = vec(tamanho_a, 0, 0), color = color.white)
asa = box(pos = vec(-60, 40 + (raio_a/2), 0), size = vec(5, 0.5, 15), color = color.white)
aeromodelo = compound([fuselagem, asa],make_trail = 1, trail_type="points", interval = 200)

carga = sphere(pos = vec(-60, 40 - (raio_a), 0), radius = raio_c, color = color.red, make_trail = True)


#Tempo de queda
tempo_queda = sqrt(2 * (40 - (raio_a + raio_c)) / 9.8)

#Alcance
alcance = 15 * tempo_queda

#Animação
while tempo < 8:
    rate(2/dt)
    vx += ax * dt
    aeromodelo.pos.x += vx * dt
    carga.pos.x += vx * dt
    tempo += dt
   
    if  -0.001 <= carga.pos.x >= 0.001:
        
        vy += ay * dt
        carga.pos.y += vy * dt
        tempo_total = tempo - 4
        
        
        
        if carga.pos.y <= (0.5):
            distancia = abs(0 - carga.pos.x)
            print(f"Considerando o método de Euler-Cromer, o tempo de queda foi: {tempo_total:.2f} s e a distância percorrida foi: {distancia:.2f} m.")
            print(f"Considerando as equações do MRU e MRUV o tempo de queda foi: {tempo_queda:.2f} s e o alcance foi: {alcance:.2f} m. ")
            print(f"Podemos considerar que os valores computacionais e teóricos concordam, tendo uma pequena variação por conta de aproximações e do dt.")
            break
