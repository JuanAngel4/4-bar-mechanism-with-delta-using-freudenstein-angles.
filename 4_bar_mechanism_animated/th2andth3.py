import numpy as np
from scipy.optimize import fsolve

def freudenstein_angles(L1, L2, L3, L4, th2):
    """
    Calcula los ángulos th3 y th4 usando las ecuaciones de Freudenstein,
    dadas las longitudes de las barras y el ángulo th2 en radianes.

    Parámetros:
    - L1, L2, L3, L4: Longitudes de las barras
    - th2: Ángulo de entrada (en radianes)

    Retorna:
    - th3, th4: Ángulos del eslabón acoplador y del eslabón de salida (en radianes)
    """

    # Coeficientes de Freudenstein
    K1 = L1 / L2
    K2 = L1 / L4
    K3 = (L1**2 + L2**2 - L3**2 + L4**2) / (2 * L2 * L4)
    K4 = L1 / L3
    K5 = (-L1**2 - L2**2 - L3**2 + L4**2) / (2 * L2 * L3)

    # Ecuaciones de Freudenstein para th3 y th4
    A = np.cos(th2)*(1 - K2) + K3 - K1
    B = -2 * np.sin(th2)
    C = -np.cos(th2)*(1 + K2) + K3 + K1
    D = np.cos(th2)*(1 + K4) + K5 - K1
    E = -2 * np.sin(th2)
    F = np.cos(th2)*(K4 - 1) + K1 + K5

    # Resolución cuadrática: arctan de las soluciones
    try:
        th3 = 2 * np.arctan((-E - np.sqrt(E**2 - 4*D*F)) / (2*D))
        th4 = 2 * np.arctan((-B - np.sqrt(B**2 - 4*A*C)) / (2*A))
    except ValueError:
        th3, th4 = np.nan, np.nan  # Si hay raíces negativas

    return th2,th3, th4,0


import numpy as np
from scipy.optimize import fsolve

def freudenstein_angles2(L1, L2, L3, L4, th2):
    """
    Calcula los ángulos th3 y th4 usando Freudenstein como estimación inicial
    y luego ajusta con fsolve para mantener la rigidez del mecanismo.

    Parámetros:
    - L1, L2, L3, L4: Longitudes de las barras
    - th2: Ángulo de entrada (en radianes)

    Retorna:
    - th2, th3, th4, th5=0 (placeholder por compatibilidad)
    """

    # ------------------------------
    # Paso 1: Estimación inicial usando Freudenstein
    K1 = L1 / L2
    K2 = L1 / L4
    K3 = (L1**2 + L2**2 - L3**2 + L4**2) / (2 * L2 * L4)
    K4 = L1 / L3
    K5 = (-L1**2 - L2**2 - L3**2 + L4**2) / (2 * L2 * L3)

    A = np.cos(th2)*(1 - K2) + K3 - K1
    B = -2 * np.sin(th2)
    C = -np.cos(th2)*(1 + K2) + K3 + K1
    D = np.cos(th2)*(1 + K4) + K5 - K1
    E = -2 * np.sin(th2)
    F = np.cos(th2)*(K4 - 1) + K1 + K5

    try:
        th3_guess = 2 * np.arctan((-E - np.sqrt(E**2 - 4*D*F)) / (2*D))
        th4_guess = 2 * np.arctan((-B - np.sqrt(B**2 - 4*A*C)) / (2*A))
    except ValueError:
        return th2, np.nan, np.nan, 0

    # ------------------------------
    # Paso 2: Corrección con fsolve (cerrar lazo vectorial)
    def loop_closure_eqs(vars):
        th3, th4 = vars

        # Coordenadas vectoriales
        x_eq = L2 * np.cos(th2) + L3 * np.cos(th3) - L4 * np.cos(th4) - L1
        y_eq = L2 * np.sin(th2) + L3 * np.sin(th3) - L4 * np.sin(th4)
        return [x_eq, y_eq]

    solution, info, ier, msg = fsolve(loop_closure_eqs, [th3_guess, th4_guess], full_output=True)

    if ier != 1:
        # No convergió
        return th2, np.nan, np.nan, 0

    th3_corrected, th4_corrected = solution

    return th2, th3_corrected, th4_corrected, 0

import numpy as np

def calcular_rango_double_rocker(L1, L2, L3, L4, resolucion=1):
    """
    Calcula el rango de th2 para el cual hay una solución válida (th3 y th4 reales).
    Sirve para mecanismos tipo Double Rocker (todos los eslabones oscilan).
    """
    th2_vals = np.radians(np.arange(0, 360, resolucion))
    angulos_validos = []

    for th2 in th2_vals:
        angulos = freudenstein_angles2(L1, L2, L3, L4, th2)
        if not np.any(np.isnan(angulos)):
            angulos_validos.append(th2)

    if len(angulos_validos) < 2:
        raise ValueError("No se encontraron suficientes ángulos válidos para formar un rango.")

    th2_min = np.min(angulos_validos)
    th2_max = np.max(angulos_validos)
    print(f"Rango de th2 válido: {np.degrees(th2_min):.2f}° a {np.degrees(th2_max):.2f}°")

    return th2_min, th2_max
