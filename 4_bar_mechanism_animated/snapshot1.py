#Importaciones
import numpy as np
from math import radians, pi
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import calculos_rebolutas as cr
import th2andth3 as thetas
import animation_4bar as a4bar
#PRIMERO, CALCULAMOS ANGULOS MAXIMOS Y MINIMOS PARA LOS CASOS DEFINIDOS

def giro_360():
    theta_min = (np.radians(2*np.pi))
    theta_max = (np.radians(2*np.pi))
    theta1 = (np.sin(0))
    caso360_list=[theta1]
    return caso360_list

def giro_MediaLuna():
    #Caso1 - Angulos minimos y maximos distintos (3)
    
    numerador1_MediaLuna = (L4**2)+(L1**2)-((L2+L3)**2)
    denominador1_MediaLuna = 2*(L4)*(L1)
    angulo_min_caso1 = np.radians(np.arccos(numerador1_MediaLuna/denominador1_MediaLuna))

    numerador2_MediaLuna = (L4**2)+((L1+L2)**2)-(L3**2)
    denominador2_MediaLuna = 2*(L4)*(L1+L2)
    angulo_max_caso1 = np.radians(np.arccos(numerador2_MediaLuna/denominador2_MediaLuna))
    theta1=angulo_min_caso1
    print("El angulo minimo es ", (np.rad2deg(angulo_min_caso1))," y el angulo maximo es ",(np.rad2deg(angulo_max_caso1)))
    caso1_list = [theta1,angulo_min_caso1,angulo_max_caso1]
    return caso1_list
        
def angulo_max_y_min_iguales():
    
    #CASO3: ANGULO MAX Y MIN IGUALES (4,5,6)
    numerador1_caso1 = (L2-L3)-(L4**2)-(L2**2)
    denominador1_caso1 = (2*L4*L1)
    angulo_max_caso2 = np.radians(np.arccos(numerador1_caso1/denominador1_caso1)*(-1))
    angulo_min_caso2 = np.radians(np.arccos(numerador1_caso1/denominador1_caso1))
    theta_1=angulo_min_caso2
    print("El angulo minimo es ", (np.rad2deg(angulo_min_caso2))," y el angulo maximo es ",(np.rad2deg(angulo_max_caso2)))
    caso2_list = [theta_1,angulo_max_caso2,angulo_min_caso2]
    return caso2_list




L1 = int(input("Ingrese longitud de L1; ")) #barra izquierda
L2 = int(input("Ingrese longitud de L2; ")) #barra que esta arriba (generalmente)
L3 = int(input("Ingrese longitud de L3; ")) # barra derecha
L4 = int(input("Ingrese longitud de L4; ")) #barra suelo
#velocity = float(input("Ingrese la velocidad de animacion(0.5 recomendado): "))
fps = int(input("Ingrese fps de la animacion(60 recomendado): "))
#delta- TRIANGULO EQUILATERO
L5 = L2
L6 = L2

barras = [L1, L2, L3, L4]
barras.sort()
s = min(barras) #longitud barra más corta
l = max(barras) #longitud barra más largo
p = barras[1] #longitud del barra restante
q = barras[2] #longitud de barra restante
theta_0 = 0
num_calculos = 100
#CRANK ROCKER (1)
if ((s + l <= p + q) and (L1 != s)):
    print("Su caso es Cranck Rocker (Grashoff)")

    # Número de pasos (de 0 a 360 grados)
    n = 360

    # Crear arrays para los ángulos theta1, theta2, theta3
    resultados = np.zeros((n, 3))

    for i in range(n):
        angulos = thetas.th23(L1, L2, L3, L4,np.radians(i))
        if angulos is not None:
            resultados[i, :] = angulos
        else:
            # Puedes poner un valor por defecto o manejar el error
            resultados[i, :] = resultados[i-1, :] if i > 0 else [0,0,0]

    # Separar los ángulos para usar
    theta_1_array = resultados[:, 0]
    theta_2_array = resultados[:, 1]

    # Calcular posiciones para todos los frames usando tu función en cr
    REV_A, REV_B, REV_C, REV_D, REV_E = cr.generar_posiciones(theta_1_array, theta_2_array, L1, L2, L3, L4, L5)

    # Ahora llamas la animación con los arrays de posiciones
    a4bar.animar_una_barra(REV_A, REV_C, REV_B, REV_D, REV_E,fps, l,barra_elegida=1)
    a4bar.b4anim(REV_A, REV_C, REV_B, REV_D, REV_E,fps, l)

"""
    
#DOUBLE ROCKER (2)
elif ((((s + l) <= (p + q))) and ((L4 == s) and (L3 == l))):
    lista_retornada_giro_360 = giro_360()
    thetas.th23(lista_retornada_giro_360[0])
    print("Su caso es Double Rocker (Grashoff)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)

#ROTATING COUPLER (3)
elif ((((s + l) <= (p + q))) and ((L2 == s) and (L3 == l))):
    lista_retornada_medialuna = giro_MediaLuna()
    thetas.th23(lista_retornada_medialuna[0])
    print("Su caso es Rotating Coupler (Grashoff)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)
#NON-GRASHOFF / # DOUBLE ROCKER OUTWARD-OUTWARD (4)
elif ((((s + l) > (p + q))) and ((L3 == s) and (L2 == l))):
    lista_retornada_angulomaxmin = angulo_max_y_min_iguales()
    thetas.th23(lista_retornada_angulomaxmin[0])
    print("Su caso es Double Rocker Outward-Outward (Non-Grashoff)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)

#NON-GRASHOFF / # DOUBLE ROCKER INWARD-INWARD (5)
elif ((((s + l) > (p + q))) and ((L1 == s) and (L4 == l))):
    lista_retornada_angulomaxmin = angulo_max_y_min_iguales()
    thetas.th23(lista_retornada_angulomaxmin[0])
    print("Su caso es Double Rocker Inward-Inward (Non-Grashoff)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)

#NON-GRASHOFF / # DOUBLE ROCKER OUTWARD-INWARD (6)
elif ((((s + l) > (p + q))) and ((L2 == s) and (L1 == l))):
    lista_retornada_angulomaxmin = angulo_max_y_min_iguales()
    thetas.th23(lista_retornada_angulomaxmin[0])
    print("Su caso Double Rocker Outward Inward (Non-Grashoff)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)

#GRASHOFF ESPECIAL 1 / # DELTA KITE (7)- CASO PERRITO BRO
elif ((((s + l) == (p + q))) and ((L2 == L4) and (L1 == L4))):
    lista_retornada_giro_360 = giro_360()
    thetas.th23(lista_retornada_giro_360[0])
    print("Su caso es Delta Kite (Grashoff Especial)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)

#GRASHOFF ESPECIAL 2 / # PARALEL 1 (8)- CASO PERRITO BRO
elif ((((s + l) == (p + q))) and ((L1 == L3) and (L2 == L4)) and ((L2 > L3) and (L4 > L1))):
    lista_retornada_giro_360 = giro_360()
    thetas.th23(lista_retornada_giro_360[0])
    print("Su caso es PARALEL 1 (Grashoff Especial)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)
#GRASHOFF ESPECIAL 3 / # PARALEL 2 (9)- CASO PERRITO BRO
elif ((((s + l) == (p + q))) and ((L1 == L3) and (L2 == L4)) and ((L2 < L3) and (L4 <L1))):
    lista_retornada_giro_360 = giro_360()
    thetas.th23(lista_retornada_giro_360[0])
    print("Su caso es PARALEL 2 (Grashoff Especial)")
    lista_theta2_and_theta_3 = thetas.th23()
    theta_1=(lista_theta2_and_theta_3[0])
    theta_2=(lista_theta2_and_theta_3[1])
    theta_3=(lista_theta2_and_theta_3[2])
    cr.crA()
    cr.crB(theta_1)
    cr.crC(theta_1,theta_2)
    cr.crD(theta_0)
    cr.crE(theta_1)
    
else:
    print("El caso especificado no existe o no está especificado")
"""