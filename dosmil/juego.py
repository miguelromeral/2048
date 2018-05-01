'''
Created on 1 may. 2018

@author: miguelangel.garciar
'''
from random import randint, random
from __builtin__ import True

# Posibles valores de las casillas.
VALORES = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
           32768, 65536, 131072, 262144, 524288, 1048576)


# Posibles tamaños de tablero.
TABLEROS = (3, 4, 5, 6)

# Probabilidad de que aparezca un 4 en lugar de un 2.
PR_CUATRO = 0.15

class Juego(int):
    '''
    Clase en la que se encuentra el tablero.
    '''
    
    def __init__(self, longitud):
        '''
        Constructor del Tablero.
        '''
        self.longitud = longitud
        self.tablero = [[None] * longitud] * longitud
        self.puntuacion = 0
        
        
    def valida(self, x, y):
        '''
        Indica si las coordenadas X,Y son validas. Empiezan por 0 y terminan en longitud - 1
        '''
        return x >= 0 and x < self.longitud and y >= 0 and y < self.longitud
    
    
    def vacia(self, x, y):
        '''
        Indica si una casilla esta vacia (antes habrá que comprobar las coordenadas con: valida(x,y).
        '''
        return self.tablero[x][y] == None
    
    
    def aleatorio(self):
        '''
        Retorna un valor aleatorio entre 0 y Longitud - 1.
        '''
        return randint(0, self.longitud - 1)
    
    
    def nueva_casilla(self): 
        valida = False
        x = -1
        y = -1
        while not valida:
            x = self.aleatorio()
            y = self.aleatorio()
            if self.vacia(x,y):
                valida = True
        # Valor a poner, un 2 o un 4.
        valor = -1
        if random() < PR_CUATRO:
            valor = 4
        else:
            valor = 2
        self.tablero[x][y] = valor
        
        