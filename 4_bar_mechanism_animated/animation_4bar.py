import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def b4anim(posa, posb, posc, posd, pose, fps, l):
    """
    Anima un sistema de 4 barras con un triángulo adicional (barra B→E y C→E).

    Parámetros:
    - posa: (n, 2) posiciones del punto A (fijo, origen de L1).
    - posb: (n, 2) posiciones del punto B (extremo de L1).
    - posc: (n, 2) posiciones del punto C (extremo de L2).
    - posd: (n, 2) posiciones del punto D (fijo, extremo de L3).
    - pose: (n, 2) posiciones del punto E (forma el triángulo con B y C).
    - fps: cuadros por segundo de la animación.
    - l: escala del gráfico.
    """

    # Convertir a arrays numpy por seguridad
    posa = np.array(posa)
    posb = np.array(posb)
    posc = np.array(posc)
    posd = np.array(posd)
    pose = np.array(pose)

    n_frames = posa.shape[0]

    fig, ax = plt.subplots()
    ax.set_xlim(-l, l + 10)
    ax.set_ylim(-l, l + 10)
    ax.set_aspect('equal')
    ax.set_title("Sistema de 4 barras con triángulo móvil")
    ax.grid(True)

    # Dibujar las barras como líneas conectando rebolutas
    barra_L1, = ax.plot([], [], 'ro-', lw=3, label="L1 (A→B)")
    barra_L2, = ax.plot([], [], 'go-', lw=3, label="L2 (B→C)")
    barra_L3, = ax.plot([], [], 'bo-', lw=3, label="L3 (C→D)")
    barra_BE, = ax.plot([], [], 'mo--', lw=2, label="B→E (Triángulo)")
    barra_CE, = ax.plot([], [], 'co--', lw=2, label="C→E (Triángulo)")

    def init():
        for barra in [barra_L1, barra_L2, barra_L3, barra_BE, barra_CE]:
            barra.set_data([], [])
        return barra_L1, barra_L2, barra_L3, barra_BE, barra_CE

    def update(frame):
        A = posa[frame]
        B = posb[frame]
        C = posc[frame]
        D = posd[frame]
        E = pose[frame]

        barra_L1.set_data([A[0], B[0]], [A[1], B[1]])
        barra_L2.set_data([B[0], C[0]], [B[1], C[1]])
        barra_L3.set_data([C[0], D[0]], [C[1], D[1]])
        barra_BE.set_data([B[0], E[0]], [B[1], E[1]])
        barra_CE.set_data([C[0], E[0]], [C[1], E[1]])

        return barra_L1, barra_L2, barra_L3, barra_BE, barra_CE

    anim = FuncAnimation(
        fig, update, frames=n_frames, init_func=init,
        blit=True, interval=1000 / fps
    )

    plt.legend()
    plt.show()

    return anim






import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animar_una_barra(posa, posb, posc, posd, pose, fps, l, barra_elegida=2):
    """
    Anima solo una barra del sistema de 5 barras, según la barra que se elija.

    Parámetros:
    - posa, posb, posc, posd, pose: arrays (n_frames, 2) con posiciones de cada punto en cada frame.
    - fps: cuadros por segundo.
    - l: límite para los ejes.
    - barra_elegida: número entero del 1 al 5 que indica cuál barra animar.

    Barras:
    1: posa → posb
    2: posb → posc
    3: posc → posd
    4: posb → pose
    5: posc → pose
    """

    posa = np.array(posa)
    posb = np.array(posb)
    posc = np.array(posc)
    posd = np.array(posd)
    pose = np.array(pose)

    n_frames = posa.shape[0]

    fig, ax = plt.subplots()
    ax.set_xlim(-l-5, l+5)
    ax.set_ylim(-l-5, l+5)
    ax.set_aspect('equal')
    ax.set_title(f"Animación barra {barra_elegida}")

    # Crear una línea vacía para la barra elegida
    barra, = ax.plot([], [], 'o-', lw=3, label=f"Barra {barra_elegida}")

    def init():
        barra.set_data([], [])
        return barra,

    def update(frame):
        pa = posa[frame]
        pb = posb[frame]
        pc = posc[frame]
        pd = posd[frame]
        pe = pose[frame]

        if barra_elegida == 1:
            xs, ys = [pa[0], pb[0]], [pa[1], pb[1]]
        elif barra_elegida == 2:
            xs, ys = [pb[0], pc[0]], [pb[1], pc[1]]
        elif barra_elegida == 3:
            xs, ys = [pc[0], pd[0]], [pc[1], pd[1]]
        elif barra_elegida == 4:
            xs, ys = [pb[0], pe[0]], [pb[1], pe[1]]
        elif barra_elegida == 5:
            xs, ys = [pc[0], pe[0]], [pc[1], pe[1]]
        else:
            xs, ys = [], []

        barra.set_data(xs, ys)
        return barra,

    anim = FuncAnimation(fig, update, frames=n_frames, init_func=init,
                         blit=True, interval=1000 / fps)

    plt.legend()
    plt.show()

    return anim
