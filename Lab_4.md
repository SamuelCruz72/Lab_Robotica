# Laboratorio No. 04 - 2025-I - Cinemática Directa - Phantom X - ROS

El objetivo de esta práctica de laboratoria es aprender a controlar los Joint Controllers de ROS para manipular los servomotores Dynamixel AX-12 del robot Phantom X Pincher a fin de ubicarlo en cualquier pose a partir de los valores de sus ángulos en las articulaciones.

## Representación del Robot Phantom X Pincher
<p align="center">
   <img src="Figuras\Lab4\Esquema Robot.png" alt="Mariposa grande" width="100"><br> 

<p align="center">
   <img src="Figuras\Lab4\DHstd.png" alt="Mariposa grande" width="100"><br> 

| i | $\theta_i$ | $d_i$ | $a_i$ | $\alpha_i$ | Offset |
|:-:|:-------:|:---:|:---:|:-------:|:------:|
| 1 | $\theta_1$ |  51 |  0  |   $\pi$/2  |    0   |
| 2 | $\theta_2$ |  0  | 110 |    0    |  $\pi$/2  |
| 3 | $\theta_3$ |  0  | 108 |    0    |    0   |
| 4 | $\theta_4$ |  0  |  0  |   $\pi$/2  |  $\pi$/2  |
| 5 | $\theta_5$ |  77 |  0  |    0    |    0   |
