from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNA: JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA IV - QUESTÃO 2 - LETRA B

# Dados do programa
inclinacao = atan(0.2)       # Inclinação do terreno
direcao = radians(30)        # Direção de lançamento do projétil
v0 = 30                      # Velocidade de lançamento do projétil
g = vec(0, -9.8, 0)          # Vetor aceleração
t = 0                        # Tempo inicial
dt = 0.01                    # Passo
espessura = 1                # Espessura do terreno
raio = 0.5                   # Raio do projétil
comprimento = 100            # Comprimento do terreno

# Criando os objetos
projetil = sphere(pos=vec(raio, raio + espessura/2, 0), radius=raio, color=color.red, make_trail=True)
terreno = box(pos=vec(comprimento/2, (comprimento/2) * 0.22, 0), size=vec(comprimento, espessura, 5), axis=vec(cos(inclinacao), sin(inclinacao), 0), color=color.green)

# Ajustando a cena
scene.center = vec(comprimento/2, (comprimento/2) * 0.22, 0)
scene.pause()

# Cálculo das componentes da velocidade inicial
vx0 = v0 * cos(direcao)
vy0 = v0 * sin(direcao)

# Inicialização das variáveis de posição e velocidade
projetil.velocidade = vec(vx0, vy0, 0)
projetil.aceleracao = vec(0, -9.8 * cos(inclinacao), 0)

# Simulação
alcance = 0  # Inicialize o alcance
while projetil.pos.y >= 0:
    # Verifica se o projétil colidiu com o terreno
    if projetil.pos.y <= terreno.pos.y + terreno.size.y / 2:
        rate(2/dt)
        projetil.velocidade = projetil.velocidade + projetil.aceleracao * dt
        projetil.pos = projetil.pos + projetil.velocidade * dt
        alcance = projetil.pos.x
        break

print(f"Alcance ao longo do plano inclinado: {alcance:.3f} m.")