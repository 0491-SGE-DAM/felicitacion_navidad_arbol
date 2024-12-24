#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

# Defino constantes ANSII para los colores
GREEN = '\033[92m'  # Verde brillante
RED_INTENSE = "\033[91m"   # Rojo brillante
RED_SOFT = "\033[31m"     # Rojo menos intenso
YELLOW_INTENSE = "\033[93m"  # Amarillo brillante
YELLOW_SOFT = "\033[33m"    # Amarillo menos intenso
WHITE = "\033[97m"  # Blanco brillante
GRAY = "\033[90m"    # Gris
RESET = "\033[0m"    # Resetear color

MESSAGE = "¡El Departamento de Informática del CEED os desea Feliz Navidad!"

# Opciones de decoraciones
DECORATIONS = [GREEN + '*', RED_INTENSE + 'o', YELLOW_INTENSE + 'x', WHITE + '+']

def generate_static_tree(levels):
    """Genera un árbol con decoraciones aleatorias"""
    xts_tree = ['\n','\n']
    for i in range(1, levels + 1):
        row = ''
        for j in range(2 * i - 1):
            # Uso probabilidad para decidir si es decoración o rama verde
            if random.random() < 0.2:  # 20% de probabilidad de decoración
                decoration = random.choice(DECORATIONS[1:])  # Sin incluir el verde
            else:
                decoration = DECORATIONS[0]  # Rama verde
            row += decoration
        xts_tree.append(' ' * (len(MESSAGE) // 2 - levels) + ' ' * (levels - i) + row + RESET)
    return xts_tree

def display_tree_with_blinking(levels, frames=10, delay=0.5):
    """Muestra el árbol con parpadeo alternando colores."""
    trunk = '|||'
    
    # Generar el árbol fijo con decoraciones
    xts_tree = generate_static_tree(levels)
    lights_on = True

    for frame in range(frames):

        if frame % 4 == 0:
            lights_on = not lights_on

        # Alterno entre tonos intensos y suave .
        # Para darle cierta aleatoriedad pongo los valores cruzados e incluso con parametros random
        red = RED_INTENSE if lights_on and random.random() > 0.6 else RED_SOFT
        yellow = YELLOW_SOFT if lights_on and random.random() < 0.6 else YELLOW_INTENSE
        white = WHITE if lights_on else GRAY

        # Mostrar el árbol con colores alternados
        for row in xts_tree:
            modified_row = (
                row.replace(RED_INTENSE, red)
                .replace(YELLOW_INTENSE, yellow)
                .replace(WHITE, white)
            )
            print(modified_row)
        
        # Mostrar el tronco
        for _ in range(3):  # Número de líneas del tronco
            print(RED_INTENSE + ' ' * (len(MESSAGE) // 2 - levels - 2 ) , ' ' * (levels - len(trunk) // 2) + trunk + RESET)

        # Mensaje de felicitación
        print(YELLOW_INTENSE + '\n' + ' ' * (len(MESSAGE) - frame) + MESSAGE[:frame] + RESET)
        
        # Esperar antes de mostrar el siguiente frame
        time.sleep(delay)
        
        # Limpio la pantalla para el siguiente frame
        print('\033[H\033[J', end='')

# Parámetros del árbol
niveles = 10  # Número de niveles del árbol
display_tree_with_blinking(niveles, frames=len(MESSAGE) + 7, delay=0.2)

