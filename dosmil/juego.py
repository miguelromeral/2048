# -*- coding: utf-8 -*-    
'''
Created on 1 may. 2018

@author: miguelangel.garciar
'''
from random import randint, random
import sys
from __builtin__ import True

class Juego(int):
    '''
    Clase en la que se encuentra el tablero.
    '''
    
    # Posibles valores de las casillas.
    VALORES = (None, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
               32768, 65536, 131072, 262144, 524288, 1048576)
    
    
    # Posibles tama�os de tablero.
    TABLEROS = (3, 4, 5, 6, 7, 8)
    
    # Probabilidad de que aparezca un 4 en lugar de un 2.
    PR_CUATRO = 0.09
    
    def __init__(self, longitud):
        '''
        Constructor del Tablero.
        '''
        self.longitud = longitud
        columnas = []
        for i in range(0, longitud):
            fila = []
            for j in range(0, longitud):
                fila.append(None)
            columnas.append(fila)
        self.tablero = columnas
        self.puntuacion = 0
        
        
    def valida(self, x, y):
        '''
        Indica si las coordenadas X,Y son validas. Empiezan por 0 y terminan en longitud - 1
        '''
        return x >= 0 and x < self.longitud and y >= 0 and y < self.longitud
    
    
    def vacia(self, x, y):
        '''
        Indica si una casilla esta vacia (antes habr� que comprobar las coordenadas con: valida(x,y).
        '''
        return self.tablero[x][y] == None
    
    
    def aleatorio(self):
        '''
        Retorna un valor aleatorio entre 0 y Longitud - 1.
        '''
        return randint(0, self.longitud - 1)
    
    
    def nueva_casilla(self): 
        '''
        Rellena una casilla con un 2 o 4 de forma aleatoria (si hay hueco). Retorna True si se pudo.
        '''
        valida = False
        contador = 200
        x = -1
        y = -1
        while ((not valida) and (contador > 0)):
            x = self.aleatorio()
            y = self.aleatorio()
            if self.vacia(x,y):
                valida = True
            else:
                contador-= 1
        if contador == 0:
            # Finalizara el juego, ya lo ha intentado suficientes veces.
            return False
        # Valor a poner, un 2 o un 4.
        valor = -1
        if random() < self.PR_CUATRO:
            valor = 4
        else:
            valor = 2
        self.tablero[x][y] = valor
        return True
        
        
    def imprimir(self):
        print('-----------------------')
        i = 0
        while i < self.longitud:
            for el in self.tablero[i]:
                if el == None:
                    sys.stdout.write(' - ')
                else:
                    #print(' {} '.format(el), end="\t")
                    sys.stdout.write(' {} '.format(el))
            print('')
            i += 1
        print('-----------------------')
        return ''
                
        
        
        
        
        