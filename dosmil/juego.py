# -*- coding: utf-8 -*-    
'''
Created on 1 may. 2018

@author: miguelangel.garciar
'''
from random import randint, random
#from texttable import Texttable
import sys
import copy
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
    PR_CUATRO = 0.1
    
    # Tamaño de una casilla
    W_CELL = 10
    
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
            valor = 2
        else:
            valor = 1
        self.tablero[x][y] = valor
        return True
        
        
    def imprimir(self):
        print('-------------------------------------------------------')
        print(' * Puntuacion: {} \n'.format(self.puntuacion))
        i = 0
        while i < self.longitud:
            for el in self.tablero[i]:
                if el == None:
                    el = '-'
                else:
                    el = self.VALORES[int(el)]
                sys.stdout.write('{}'.format(el).center(self.W_CELL))
            print('\n')
            i += 1
        print('-------------------------------------------------------')
        return ''
    
    def intercambiar(self, x1, y1, x2, y2):
        '''
        Intercambia la posicion de dos casillas
        '''
        aux = self.tablero[x1][y1]
        self.tablero[x1][y1] = self.tablero[x2][y2]
        self.tablero[x2][y2] = aux
    
    
    def unir_dos_casillas(self, x1, y1, x2, y2):
        '''
        Une dos casillas. La casilla que se almacena es x1,y1. La otra se queda vacia
        '''
        valor1 = self.tablero[x1][y1]
        valor2 = self.tablero[x2][y2]
        if valor1 == valor2 and not valor1 is None:
            self.tablero[x2][y2] = None
            self.tablero[x1][y1] = valor1 + 1
            return self.VALORES[valor1 + 1]
        return 0
    
    
    def llevar_casilla_izquierda(self, x, y):
        '''
        Mueve la casilla X,Y a la izquierda
        '''
        aux = y - 1                 # Empezamos a mirar la siguiente casilla
        if aux >= 0:                # Siempre que no nos salgamos por la izquierda
            if self.vacia(x, aux):
                # Si esta vacia, la intercambiamos, y volveremos a comprobar si se puede
                # llevar a la izquierda la que acabamos de intercambiar (la que tiene valor,
                # la otra esta vacia). Llegara un punto en el que dejara de ir a la izquierda.
                self.intercambiar(x, y, x, aux)
                self.llevar_casilla_izquierda(x, aux)
    
    
    def desplazamientos_izquierda(self):
        '''
        Lleva las casillas necesarias a la izquierda
        '''
        # Desplazamos a la izquierda todas las casillas (sin que se junten)
        for x in range(0, self.longitud):               # Para cada fila:
            for nueva in range(1, self.longitud):       # Para cada columna (desde la 1 hasta n-1)
                # 1, porque la 0 no hace falta comprobarla.
                self.llevar_casilla_izquierda(x, nueva) # Movemos todas las demas casillas
    
    
    def movimiento_izquierda(self, sumar):
        '''
        Realiza el movimiento del tablero a la izquierda. Se indica si se deben sumar los puntos o no.
        '''
        self.anterior = list(self.tablero)
        self.desplazamientos_izquierda()
        # Unimos las que esten juntas:
        puntos = 0
        for x in range(0, self.longitud):               # Para cada fila:
            for nueva in range(0, self.longitud - 1):       # Para cada columna (desde la 0 hasta n-2)
                puntos += self.unir_dos_casillas(x, nueva, x, nueva + 1) 
        self.desplazamientos_izquierda()
        if sumar:
            self.puntuacion += puntos
        return puntos
        
    
    def tableros_diferentes(self, nuevo):
        '''
        Indica si dos tableros son diferentes
        '''
        for x in range(0, self.longitud):
            for y in range(0, self.longitud):
                if self.tablero[x][y] != nuevo[x][y]:
                    return True
        return False
        
        
    def exportar_tablero(self):
        '''
        Devuelve una copia del tablero
        '''
        filas = []
        for el in self.tablero:
            columnas = []
            for ot in el:
                columnas.append(ot)
            filas.append(columnas)
        return filas
    
    
    def importar_tablero(self, nuevo):
        '''
        Copia el nuevo tablero en el propio
        '''
        filas = []
        for el in nuevo:
            columnas = []
            for ot in el:
                columnas.append(ot)
            filas.append(columnas)
        self.tablero = filas

        
    def movimiento_posible(self, mov):
        '''
        Indica si hay un movimiento posible. mov es w,a,s,d (arriba, izquierda, abajo, derecha)
        '''
        diferentes = False
        anterior = self.exportar_tablero()
        if mov == 'w':
            pass
        elif mov == 'a':
            self.movimiento_izquierda(False)
        elif mov == 's':
            pass
        elif mov == 'd':
            pass
        diferentes = self.tableros_diferentes(anterior)
        self.importar_tablero(anterior)
        return diferentes
    
    '''
    def imprimir2(self):
        table = Texttable()
        print('-------------------------------------------------------')
        print(' * Puntuacion: {} \n'.format(self.puntuacion))
        i = 0
        fila =  []
        while i < self.longitud:
            for el in self.tablero[i]:
                if el == None:
                    el = '-'
                else:
                    print('el = {}'.format(el))
                    el = self.VALORES[int(el)]
                    print('ahora es {}'.format(el))
                fila.append(el.center(self.W_CELL))
            table.add_row(fila, header=False)
            fila = []
            i += 1
        print table.draw()
        print('-------------------------------------------------------')
    '''   
        
        
        