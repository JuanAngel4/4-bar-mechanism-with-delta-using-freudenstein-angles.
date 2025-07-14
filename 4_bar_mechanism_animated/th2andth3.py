import numpy as np

def th23(theta_1, L1, L2, L3, L4, rama=1):
    """
    Calcula los ángulos theta_2 y theta_3 para un mecanismo de 4 barras dado theta_1.
    
    Parámetros:
    - theta_1: ángulo de la barra 1 (input)
    - L1, L2, L3, L4: longitudes de las barras
    - rama: 1 o 2, para elegir la configuración de la solución (rama 1: beta + alpha, rama 2: beta - alpha)
    
    Retorna:
    - array con [theta_1, theta_2, theta_3] o None si no hay solución válida
    """

    x = L1 * np.cos(theta_1)
    y = L1 * np.sin(theta_1)

    D = np.sqrt((L4 - x)**2 + y**2)

    if D > (L2 + L3) or D < abs(L2 - L3):
        return None

    cos_alpha = (L3**2 + D**2 - L2**2) / (2 * L3 * D)
    if abs(cos_alpha) > 1:
        return None

    alpha = np.arccos(cos_alpha)
    beta = np.arctan2(y, L4 - x)

    if rama == 1:
        theta_3 = beta + alpha
    elif rama == 2:
        theta_3 = beta - alpha
    else:
        raise ValueError("El parámetro 'rama' debe ser 1 o 2.")

    Bx, By = x, y
    Cx = L4 + L3 * np.cos(theta_3)
    Cy = L3 * np.sin(theta_3)

    vec_BC_x = Cx - Bx
    vec_BC_y = Cy - By
    theta_2 = np.arctan2(vec_BC_y, vec_BC_x)

    return np.array([theta_1, theta_2, theta_3])

import numpy as np

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

    return th3, th4
