import numpy as np
#Para los casos definidos por un giro de 360 grados
def crA():
    L1_X = 0 
    L1_Y = 0

    pos_a = np.array([L1_X,L1_Y])
    return pos_a

def crB(theta_1,L1):
    L1_X = L1*(np.cos(theta_1))
    L1_Y = L1*(np.sin(theta_1))
    pos_b = np.array([L1_X,L1_Y])
    return pos_b

def crC(theta_1,theta_2,L1,L2):
    L1_X = L1*(np.cos(theta_1))
    L1_Y = L1*(np.sin(theta_1))
    L2_X = L2*(np.cos(theta_2))
    L2_Y =  L2*(np.sin(theta_2))
    pos_c = np.array([L1_X+L2_X,L1_Y+L2_Y])
    return pos_c

theta_0=(0)

def crD(theta_0,L4):
    L4_X = L4
    L4_Y = 0
    pos_d = np.array([L4_X,L4_Y])
    return pos_d

def crE(theta_1,L1,L5):
    L1_X = L1*(np.cos(theta_1))
    L1_Y = L1*(np.sin(theta_1))
    L5_X = L5*(np.cos(1.0472))
    L5_Y = L5*(np.sin(1.0472))
    pos_e = np.array([(L1_X+L5_X),(L1_Y+L5_Y)])
    return pos_e

def generar_posiciones(theta_1_array, theta_2_array, L1, L2, L3, L4, L5):
    n = len(theta_1_array)
    m_pos_a = np.zeros((n, 2))
    m_pos_b = np.zeros((n, 2))
    m_pos_c = np.zeros((n, 2))
    m_pos_d = np.zeros((n, 2))
    m_pos_e = np.zeros((n, 2))

    for i in range(n):
        theta_1 = theta_1_array[i]
        theta_2 = theta_2_array[i]

        m_pos_a[i] = crA()
        m_pos_b[i] = crB(theta_1, L1)
        m_pos_c[i] = crC(theta_1, theta_2, L1, L2)
        m_pos_d[i] = crD(0, L4)  # fija
        m_pos_e[i] = crE(theta_1, L1, L5)

    return m_pos_a, m_pos_b, m_pos_c, m_pos_d, m_pos_e



import matplotlib.pyplot as plt

# Parámetros
L1 = 10  # longitud fija de la barra 1

# Crear array de ángulos de 0 a 360 grados, en radianes
n_pasos = 360
theta_1_array = np.linspace(0, 2*np.pi, n_pasos)

# Array para almacenar posiciones de B
pos_b_array = np.zeros((n_pasos, 2))

# Calcular posiciones para cada ángulo
for i, th in enumerate(theta_1_array):
    pos_b_array[i, :] = crB(th, L1)

# Imprimir algunas posiciones para comprobar
print("Primeras 5 posiciones de B:")
print(pos_b_array[:5])

print("Últimas 5 posiciones de B:")
print(pos_b_array[-5:])

# Opcional: graficar el recorrido de la reboluta B
plt.figure(figsize=(6,6))
plt.plot(pos_b_array[:,0], pos_b_array[:,1], label="Trayectoria reboluta B")
plt.scatter([0], [0], color='red', label='Revoluta A (fija)')
plt.gca().set_aspect('equal')
plt.title("Posición de reboluta B para θ₁ de 0 a 360°")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()