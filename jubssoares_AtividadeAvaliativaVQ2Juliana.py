from vpython import *
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA
#COLEGIADO DE LICENCIATURA EM FÍSICA
#DISCIPLINA: FÍSICA COMPUTACIONAL II
#ALUNOS: IAN ANTHONY SENA DA SILVA E JULIANA SILVA SOARES
#ATIVIDADE AVALIATIVA V - QUESTÃO 2

#Dados da questão
c = 0.20                            # Coeficiente de resistência
m = 80.0                            # Massa total (ciclista + bicicleta) em kg
v0 = 20.0                           # Velocidade inicial em m/s
f2 = -3.0                           # Força resistiva constante em N
dt = 0.01                           # Passo de tempo em segundos
t = 0.0                             # Tempo inicial
v = v0                              # Velocidade inicial
x0 = 0.0                             # Posição inicial

# Listas
tempo = [t]
velocidade = [v]

# Gráfico da Velocidade contra o Tempo
graph(title="\nMovimento do ciclista", xtitle="Tempo (s)", ytitle="Velocidade (m/s)", fast = False)

grafico = gcurve(color = vec(1.000, 0.698, 0.698), label="V(t)")


# Simulação com o método de Euler-Cromer
while v > 0.01:                     # Ajustamos o limite para 0.01 m/s para parar a simulação quando a velocidade for próxima de zero
    rate(10000)                     # Limita a taxa de quadros para visualização
    f1 = -c * v**2                  # Força de arrasto quadrático
    a = (f1 + f2) / m               # Calcula a aceleração considerando ambas as forças
    v = v + a * dt                  # Atualiza a velocidade usando o novo valor de aceleração
    x0 = x0 + v * dt                  # Atualiza a posição usando a nova velocidade
    t = t + dt                      # Atualiza o tempo
    tempo.append(t)
    velocidade.append(v)
    grafico.plot(t, v)

# Cálculo do tempo até parar
t_parar = tempo[-1]
print('Tempo até parar:', round(t_parar, 2), 'segundos')

# Cálculo da distância percorrida
d = x0
print('Distância percorrida:', round(d, 2), 'metros')

