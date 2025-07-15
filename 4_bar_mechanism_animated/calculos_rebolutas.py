import numpy as np

def crA():
    # Punto fijo tierra (origen)
    return np.array([0.0, 0.0])

def crB(th2, L2):
    """Posición de B, extremo de barra giratoria L2, con ángulo th2"""
    x = L2 * np.cos(th2)
    y = L2 * np.sin(th2)
    return np.array([x, y])

def crC(L2,L3,th2,th3):
    L2_X = L2 *np.cos(th2)
    L2_Y = L2 *np.sin(th2)
    L3_X = L3 *np.cos(th3)
    L3_Y = L3 *np.sin(th3)
    return np.array([L2_X+L3_X, L2_Y+L3_Y])

def crD(L4):
    # Punto fijo tierra para barra L4 (conecta en (L4, 0))
    return np.array([L4, 0.0])

def crE(th2, th3, L2, L3, L5):
    """
    Calcula la posición de la reboluta E, ubicada sobre la barra 5 que
    forma un triángulo con las barras L2 (A-B) y L3 (B-C).
    
    La barra 5 parte desde B y se extiende en dirección perpendicular
    (o con un offset fijo) respecto a la barra acopladora BC.
    """

    # Punto B (extremo de barra L2)
    Bx = L2 * np.cos(th2)
    By = L2 * np.sin(th2)
    B = np.array([Bx, By])

    # Punto C (extremo del acoplador L3)
    Cx = Bx + L3 * np.cos(th3)
    Cy = By + L3 * np.sin(th3)
    C = np.array([Cx, Cy])

    # Vector unitario de dirección de BC
    v_bc = C - B
    v_bc_unit = v_bc / np.linalg.norm(v_bc)

    # Vector perpendicular a BC (en sentido antihorario)
    v_perp = np.array([-v_bc_unit[1], v_bc_unit[0]])

    # Posición de E = B + L5 * dirección perpendicular a BC
    E = B + L5 * v_perp

    return E


def generar_posiciones(th2_array, th3_array, th4_array,th5_array,th6, L1, L2, L3, L4, L5):
    n = len(th2_array)
    m_pos_a = np.zeros((n, 2))
    m_pos_b = np.zeros((n, 2))
    m_pos_c = np.zeros((n, 2))
    m_pos_d = np.zeros((n, 2))
    m_pos_e = np.zeros((n, 2))

    for i in range(n):
        th2 = th2_array[i]
        th3 = th3_array[i]
        th4 = th4_array[i]
        th5 = th5_array[i]

        m_pos_a[i] = crA()                  # origen
        m_pos_b[i] = crB(th2, L2)          # extremo barra giratoria
        m_pos_c[i] = crC(L2,L3,th2,th3)  # extremo barra superior(ORIGEN B O D)
        m_pos_d[i] = crD(L4)                # barra fija derecha
        m_pos_e[i] = crE(th2, th3, L2, L3, L5)
   # punta barra 5

    return m_pos_a, m_pos_b, m_pos_c, m_pos_d, m_pos_e



