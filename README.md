Project Overview

This project follows a modular programming approach to enable a clean and user-friendly structure for animating a four-bar mechanism. Each core component of the animation is separated into dedicated modules, allowing for easy modification and reuse.
Module Descriptions:

    th2andth3
    Computes the secondary angles of the mechanism (θ₂ and θ₃) based on an input angle θ. The resulting angles are organized into matrices for further processing.

    calculos_rebolutas
    Calculates the positions of the revolute joints using the previously obtained angular data and necessary input parameters.

    animation_4bar
    Animates the four-bar mechanism by connecting the calculated node positions with bars, creating a smooth and dynamic visualization.

Execution Flow:

Input: θ from 0° to 360°
        ↓
Module: th2andth3 → Generates angle matrices
        ↓
Module: calculos_rebolutas → Generates joint position matrices
        ↓
Module: animation_4bar → Uses positions to animate the mechanism

This structure ensures modularity, clarity, and flexibility for analyzing and animating planar four-bar mechanisms.
