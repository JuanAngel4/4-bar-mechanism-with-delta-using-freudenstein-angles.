import numpy as np
from math import radians, pi
# Librerías de funciones creadas
import calculos_rebolutas as cr
import th2andth3 as thetas
import animation_4bar as a4bar

# Definición de barras con comentarios claros
L1 = 10  # Barra estática (tierra) - barra izquierda
L2 = 3# Barra giratoria (entrada) - barra que está arriba
L3 = 7  # Barra superior - barra que conecta arriba
L4 = 10 # Barra fija (tierra) - barra derecha conectada a suelo
L5 = 6
VELOCITY = 0.9
fps = 100
th6 = np.rad2deg(60)
# Parámetros adicionales
 # Longitud para barra adicional (triángulo equilátero)
L6 = np.sqrt((L5**2)+(L3**2)-(2*L5*L3*np.cos(radians(th6))))
barras = [L1, L2, L3, L4]
barras.sort()
s = min(barras)  # Barra más corta
l = max(barras)  # Barra más larga
p = barras[1]    # Segunda longitud menor
q = barras[2]    # Segunda longitud mayor

theta_0 = 0
num_calculos = 100
n = 360

# Clasificación y simulación según tipo de mecanismo de 4 barras
if (s + l <= p + q) and (L1 != s):
    print("Su caso es Crank Rocker (Grashoff)")
    tipo = "Crank Rocker"

elif ((s + l <= p + q) and (L4 == s and L3 == l)):
    print("Su caso es Double Rocker (Grashoff)")
    tipo = "Double Rocker"

elif ((s + l <= p + q) and (L2 == s and L3 == l)):
    print("Su caso es Rotating Coupler (Grashoff)")
    tipo = "Rotating Coupler"

elif ((s + l > p + q) and (L3 == s and L2 == l)):
    print("Su caso es Non-Grashoff / Double Rocker Outward-Outward")
    tipo = "Double Rocker Outward-Outward"

elif ((s + l > p + q) and (L1 == s and L4 == l)):
    print("Su caso es Non-Grashoff / Double Rocker Inward-Inward")
    tipo = "Double Rocker Inward-Inward"

elif ((s + l > p + q) and (L2 == s and L1 == l)):
    print("Su caso es Non-Grashoff / Double Rocker Outward-Inward")
    tipo = "Double Rocker Outward-Inward"

elif ((s + l == p + q) and (L2 == L4) and (L1 == L4)):
    print("Su caso es Grashoff Especial 1: Delta Kite")
    tipo = "Grashoff Especial: Delta Kite"

elif ((s + l == p + q) and (L1 == L3) and (L2 == L4) and (L2 > L3) and (L4 > L1)):
    print("Su caso es Grashoff Especial 2: Paralelo 1")
    tipo = "Grashoff Especial: Paralelo 1"

elif ((s + l == p + q) and (L1 == L3) and (L2 == L4) and (L2 < L3) and (L4 < L1)):
    print("Su caso es Grashoff Especial 3: Paralelo 2")
    tipo = "Grashoff Especial: Paralelo 2"

else:
    print("El caso especificado no existe o no está definido")
    tipo = None

# Si el tipo fue identificado, calcular los ángulos y simular
if tipo is not None:
    resultados = np.zeros((n, 4))  # Matriz para guardar ángulos th2, th3, th4 y th5
    for i in range(n):
        angulos = thetas.freudenstein_angles2(L1, L2, L3, L4, np.radians(i))
        if angulos is not None:
            resultados[i, :] = angulos
        else:
            resultados[i, :] = resultados[i-1, :] if i > 0 else [0, 0, 0, 0]

    # Separar los ángulos (th2, th3, th4, th5)
    th2_array = resultados[:, 0]
    th3_array = resultados[:, 1]
    th4_array = resultados[:, 2]
    th5_array = resultados[:, 3]

    # Calcular posiciones para todos los frames usando la función ajustada
    REV_A, REV_B, REV_C, REV_D, REV_E = cr.generar_posiciones(
        th2_array, th3_array, th4_array, th5_array, th6, L1, L2, L3, L4, L5
    )

    # Llamar animaciones con los arrays de posiciones calculados
    a4bar.b4anim(REV_A, REV_B, REV_C, REV_D, REV_E, fps, l)
