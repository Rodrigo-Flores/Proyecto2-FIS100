from colorama import Fore
from math import sin, cos, pi, sqrt
from os import *
import numpy as np
import time

system("cls")

try:
    system("pip install colorama numpy")
    system("pip3 install colorama numpy")

except:
    pass

aceleracion_gravedad = 9.81
masa_zapatilla = 0.328 # La zapatilla pesa 0.328 kilogramos
fuerza_peso = masa_zapatilla * aceleracion_gravedad # Zapatilla [N]
beta_radian = (53+90)*(pi/180) # beta = 53°

count = 0

for alpha in np.arange(0,180,0.1):
    alpha_radian = alpha * (pi/180)
    for gamma in np.arange(0,180,0.1):
        gamma_radian = gamma * (pi/180)

        ## Calcular a y b
        try:
            a = (sin(alpha_radian)*fuerza_peso)/sin(gamma_radian)
        except ZeroDivisionError:
            a = 0

        
        try:
            b = (a*sin(beta_radian))/(sin(alpha_radian))
        except ZeroDivisionError:
            b = 0


        ## calcular componentes
        # c -> peso
        # b -> Fp
        # a -> F

        F_x = b*sin(gamma_radian) # ax
        F_y = a*sin(beta_radian) # ay

        F_normal = b*cos(gamma_radian)
        F_roce = a*cos(beta_radian)
        F_peso = fuerza_peso
        
        fuerza_total_x = F_x + F_roce
        fuerza_total_y = F_normal - F_y - F_peso

        count += 1 # Intentos

        if (F_normal > F_y): # La normal debe ser mayor a al menos una de las fuerzas en Y
            if ((alpha_radian + beta_radian + gamma_radian) == pi): # Los ángulos deben sumar 180° o pi [rad]

                system("cls")

                print(
                    f"""

                    {Fore.YELLOW} Intentos: {count}

                    Componentes:
                    Fx: {F_x}
                    Fy: {F_y}
                    Normal: {F_normal}
                    Roce: {F_roce}
                    Peso: {F_peso}

                    Angulos:
                    Alpha: {alpha}
                    Beta: {beta_radian * (180/pi)}
                    Gamma: {gamma}

                    Fuerzas:
                    Peso (c): {fuerza_peso}
                    F (a): {a}
                    Fp (b): {b}

                    Fuerza Total x: {fuerza_total_x}
                    Fuerza Total y: {fuerza_total_y}

                    """
                )

                if True: # Esto se puede utilizar para ver mejor rangos de pruebas específicos
                    time.sleep(.2)
