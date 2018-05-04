# -*- coding: utf-8 -*-    
'''
Created on 1 may. 2018

@author: miguelangel.garciar
'''
import random
import sys
from __builtin__ import True

K_UP = 'w'
K_LEFT = 'a'
K_DOWN = 's'
K_RIGHT = 'd'
K_UNDO = 'u'
K_QUIT = 'q'

class Juego(int):
    '''
    Clase en la que se encuentra el tablero.
    '''
    
    # Posibles valores de las casillas.
    VALORES_1 = (None, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    VALORES_2 = (None, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
               32768, 65536, 131072, 262144, 524288, 1048576)
    VALORES_3 = (None, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969,
               14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401)
    
    VALORES_FIBONACCI = (None, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
               610, 987, 1597, 2584, 4181, 6765)
    
    VALORES=(VALORES_1, VALORES_2, VALORES_3, VALORES_FIBONACCI)
    
    # Posibles tama�os de tablero.
    TABLEROS = (3, 4, 5, 6, 7, 8)
    
    # Probabilidad de que aparezca un 4 en lugar de un 2.
    PR_CUATRO = 0.05
    
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
        self.tablero_anterior = None
        self.puntuacion = 0
        self.movimientos = 0
        #self.celdas = self.VALORES[num_cel]
        self.celdas = self.VALORES[1]
    
        
        
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
        return random.randint(0, self.longitud - 1)
    
    
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
        if random.random() < self.PR_CUATRO:
            valor = 2
        else:
            valor = 1
        self.tablero[x][y] = valor
        return True
        
        
    def imprimir(self):
        print('---------------------------------------------------------------------')
        print(' * Puntuacion: {} | Movimientos: {}\n'.format(self.puntuacion,self.movimientos))
        i = 0
        while i < self.longitud:
            for el in self.tablero[i]:
                if el == None:
                    el = '-'
                else:
                    el = self.celdas[int(el)]
                sys.stdout.write('{}'.format(el).center(self.W_CELL))
            print('\n')
            i += 1
        print('---------------------------------------------------------------------')
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
            return self.celdas[valor1 + 1]
        return 0
    
    def llevar_casilla_derecha(self, x, y):
        aux = y + 1 
        if aux < self.longitud:
            if self.vacia(x, aux):
                self.intercambiar(x, y, x, aux)
                self.llevar_casilla_derecha(x, aux)
    
    
    def desplazamientos_derecha(self):
        for x in range(0, self.longitud):  
            alreves = range(0, self.longitud - 1)
            for nueva in reversed(alreves): 
                self.llevar_casilla_derecha(x, nueva) 
    
    
    def movimiento_derecha(self, sumar):
        self.desplazamientos_derecha()
        puntos = 0
        for x in range(0, self.longitud):
            alreves = range(1, self.longitud)
            for nueva in reversed(alreves):
                puntos += self.unir_dos_casillas(x, nueva, x, nueva - 1) 
        self.desplazamientos_derecha()
        if sumar:
            self.puntuacion += puntos
        return puntos
    
    
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
    
    
    
    def llevar_casilla_arriba(self, x, y):
        aux = x - 1
        if aux >= 0:                # Siempre que no nos salgamos por la izquierda
            if self.vacia(aux, y):
                self.intercambiar(x, y, aux, y)
                self.llevar_casilla_arriba(aux, y)
    
    def desplazamientos_arriba(self):
        for y in range(0, self.longitud):               
            for nueva in range(1, self.longitud):       
                self.llevar_casilla_arriba(nueva, y)
    
    def movimiento_arriba(self, sumar):
        self.desplazamientos_arriba()
        puntos = 0
        for y in range(0, self.longitud):               # Para cada fila:
            for nueva in range(0, self.longitud - 1):       # Para cada columna (desde la 0 hasta n-2)
                puntos += self.unir_dos_casillas(nueva, y, nueva + 1, y) 
        self.desplazamientos_arriba()
        if sumar:
            self.puntuacion += puntos
        return puntos
    
    
    
    
    def llevar_casilla_abajo(self, x, y):
        aux = x + 1
        if aux < self.longitud:                # Siempre que no nos salgamos por la izquierda
            if self.vacia(aux, y):
                self.intercambiar(x, y, aux, y)
                self.llevar_casilla_abajo(aux, y)
    
    def desplazamientos_abajo(self):
        for y in range(0, self.longitud):    
            alreves = range(0, self.longitud - 1)
            for nueva in reversed(alreves):     
                self.llevar_casilla_abajo(nueva, y)
    def movimiento_abajo(self, sumar):
        self.desplazamientos_abajo()
        puntos = 0
        for y in range(0, self.longitud):   
            alreves = range(1, self.longitud)
            for nueva in reversed(alreves):
                puntos += self.unir_dos_casillas(nueva, y, nueva - 1, y) 
        self.desplazamientos_abajo()
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
        if mov == K_UP:
            self.movimiento_arriba(False)
        elif mov == K_LEFT:
            self.movimiento_izquierda(False)
        elif mov == K_DOWN:
            self.movimiento_abajo(False)
        elif mov == K_RIGHT:
            self.movimiento_derecha(False)
        diferentes = self.tableros_diferentes(anterior)
        self.importar_tablero(anterior)
        return diferentes
    
    
    def acabado(self):
        return self.movimiento_posible(K_UP) or self.movimiento_posible(K_LEFT) or self.movimiento_posible(K_DOWN) or self.movimiento_posible(K_RIGHT)
    
    
    def mover(self, mov):
        if self.movimiento_posible(mov):
            self.tablero_anterior = self.exportar_tablero()
            self.puntuacion_anterior = self.puntuacion
            if mov == K_UP:
                self.movimiento_arriba(True)
            elif mov == K_LEFT:
                self.movimiento_izquierda(True)
            elif mov == K_DOWN:
                self.movimiento_abajo(True)
            elif mov == K_RIGHT:
                self.movimiento_derecha(True)
            self.movimientos += 1
            return self.nueva_casilla()
        else:
            return True
    
    
    def deshacer(self):
        if self.tablero_anterior == None:
            return False
        self.importar_tablero(self.tablero_anterior)
        self.puntuacion = self.puntuacion_anterior
        self.tablero_anterior = None
        self.movimientos -= 1
        return True
    
    
    def mejor_jugada(self, pasos):
        if pasos == 0:
            print('Paso 0:')
            pts_w, pts_a, pts_s, pts_d = 0,0,0,0
            tablero_ahora = self.exportar_tablero()
            pts_w = self.movimiento_arriba(False)
            self.importar_tablero(tablero_ahora)
            pts_a = self.movimiento_izquierda(False)
            self.importar_tablero(tablero_ahora)
            pts_s = self.movimiento_abajo(False)
            self.importar_tablero(tablero_ahora)
            pts_d = self.movimiento_derecha(False)
            self.importar_tablero(tablero_ahora)
            
            lista = [pts_w, pts_a, pts_s, pts_d]
            maximo = max(lista)
            print('--> {} - Total: {}'.format(lista, pts_w + pts_a + pts_s + pts_d))
            print('--> Maximo: {}'.format(maximo))
            
            repetido = lista.count(maximo)
            print( '    Repetidos: {}'.format(repetido))
            if repetido == 1:
                if maximo == pts_w:
                    ch = K_UP
                elif maximo == pts_a:
                    ch = K_LEFT
                elif maximo == pts_s:
                    ch = K_DOWN
                elif maximo == pts_d:
                    ch = K_RIGHT
            else:
                lista = []
                lista_aux = []
                if maximo == pts_w:
                    lista.append(K_UP)
                else:
                    lista_aux.append(K_UP)
                    
                if maximo == pts_a:
                    lista.append(K_LEFT)
                else:
                    lista_aux.append(K_LEFT)
                    
                if maximo == pts_s:
                    lista.append(K_DOWN)
                else:
                    lista_aux.append(K_DOWN)
                    
                if maximo == pts_d:
                    lista.append(K_RIGHT)
                else:
                    lista_aux.append(K_RIGHT)

                repetir = True
                print('    Los seleccionados son: {}'.format(lista))
                print('    Los seleccionados (aux) son: {}'.format(lista_aux))
                while repetir:
                    try:
                        ch = random.choice(lista)
                        lista.remove(ch)
                        print('        Intento: {}, queda {}'.format(ch, lista))
                        if self.movimiento_posible(ch):
                            repetir = False
                        else:
                            print('        Intentamos de nuevo...')
                    except IndexError:
                        try:
                            print('Se nos acabo')
                            ch = random.choice(lista_aux)
                            lista_aux.remove(ch)
                            print('            Intento: {}, queda {}'.format(ch, lista_aux))
                            if self.movimiento_posible(ch):
                                repetir = False
                            else:
                                print('            Intentamos de nuevo...')
                        except IndexError:
                            print (' ------- Que ya no quedan mas muyayo...!')
                            #lista = [K_UP, K_LEFT, K_DOWN, K_RIGHT]
                            lista = [K_UP, K_LEFT]
                            ch = random.choice(lista)
                            print('    Intento {}'.format(ch))
                            repetir = False
 
            
            '''if maximo == 0:
                lista = [K_UP, K_LEFT, K_DOWN, K_RIGHT]
                #repetir = True
                print('    Los seleccionados son: {}'.format(lista))
                #while repetir:
                ch = random.choice(lista)
                print('    Intento {}'.format(ch))
                lista.remove(ch)
                #    if self.movimiento_posible(ch):
                #        repetir = False
                #    else:
                #        print('        Intentamos de nuevo...')
            else:
                if maximo == pts_w:
                    ch = K_UP
                elif maximo == pts_a:
                    ch = K_LEFT
                elif maximo == pts_s:
                    ch = K_DOWN
                elif maximo == pts_d:
                    ch = K_RIGHT
            '''
            print('--> Elegido: {}'.format(ch))
            print('--> Retorno: ({},{},{})'.format(ch, maximo, (pts_w + pts_a + pts_s + pts_d)))
            return (ch, maximo, (pts_w + pts_a + pts_s + pts_d))
        else:
            pts_w, pts_a, pts_s, pts_d = 0,0,0,0
            max_w, max_a, max_s, max_d = 0,0,0,0
            lista = []
            lista_pos = []
            ch = ''
            tablero_ahora = self.exportar_tablero()
            if self.movimiento_posible(K_UP):
                print(' - ARRIBA ({})'.format(pasos))
                pts_w = self.movimiento_arriba(False)
                self.nueva_casilla()
                sig = self.mejor_jugada(pasos - 1)
                pts_w += sig[1]
                max_w = sig[2]
                print(' -ARRIBA {}, Pts: {}, Max: {}'.format(pasos, pts_w, max_w))
                self.importar_tablero(tablero_ahora)
            
            if self.movimiento_posible(K_LEFT):
                print(' - IZQUIERDA ({})'.format(pasos))
                pts_a = self.movimiento_izquierda(False)
                self.nueva_casilla()
                sig = self.mejor_jugada(pasos - 1)
                pts_a += sig[1]
                max_a = sig[2]
                print(' -IZQUIERDA {}, Pts: {}, Max: {}'.format(pasos, pts_a, max_a))
                self.importar_tablero(tablero_ahora)
            
            if self.movimiento_posible(K_DOWN):
                print(' - ABAJO ({})'.format(pasos))
                pts_s = self.movimiento_arriba(False)
                self.nueva_casilla()
                sig = self.mejor_jugada(pasos - 1)
                pts_s += sig[1]
                max_s = sig[2]
                print(' -ABAJO {}, Pts: {}, Max: {}'.format(pasos, pts_s, max_s))
                self.importar_tablero(tablero_ahora)
            
            if self.movimiento_posible(K_RIGHT):
                print(' - DERECHA ({})'.format(pasos))
                pts_d = self.movimiento_arriba(False)
                self.nueva_casilla()
                sig = self.mejor_jugada(pasos - 1)
                pts_d += sig[1]
                max_d = sig[2]
                print(' -DERECHA {}, Pts: {}, Max: {}'.format(pasos, pts_d, max_d))
                self.importar_tablero(tablero_ahora)
            
            lista = [pts_w, pts_a, pts_s, pts_d]
            lista_pos = [max_w, max_a, max_s, max_d]
            print(' * RESUMEN {}, Lista: {}, Posibles: {}'.format(pasos, lista, lista_pos))
            maximo = max(lista)
            maximo_pos = max(lista_pos)
            repetido = lista.count(maximo)
            print( '    Repetidos: {}'.format(repetido))
            if repetido == 1:
                if maximo == pts_w:
                    ch = K_UP
                elif maximo == pts_a:
                    ch = K_LEFT
                elif maximo == pts_s:
                    ch = K_DOWN
                elif maximo == pts_d:
                    ch = K_RIGHT
            else:
                lista = []
                lista_aux = []
                if maximo_pos == max_w:
                    lista.append(K_UP)
                else:
                    lista_aux.append(K_UP)
                    
                if maximo_pos == max_a:
                    lista.append(K_LEFT)
                else:
                    lista_aux.append(K_LEFT)
                    
                if maximo_pos == max_s:
                    lista.append(K_DOWN)
                else:
                    lista_aux.append(K_DOWN)
                    
                if maximo_pos == max_d:
                    lista.append(K_RIGHT)
                else:
                    lista_aux.append(K_RIGHT)

                repetir = True
                print('    Los seleccionados son: {}'.format(lista))
                print('    Los seleccionados (aux) son: {}'.format(lista_aux))
                while repetir:
                    try:
                        ch = random.choice(lista)
                        lista.remove(ch)
                        print('        Intento: {}, queda {}'.format(ch, lista))
                        if self.movimiento_posible(ch):
                            repetir = False
                        else:
                            print('        Intentamos de nuevo...')
                    except IndexError:
                        try:
                            print('Se nos acabo')
                            ch = random.choice(lista_aux)
                            lista_aux.remove(ch)
                            print('            Intento: {}, queda {}'.format(ch, lista_aux))
                            if self.movimiento_posible(ch):
                                repetir = False
                            else:
                                print('            Intentamos de nuevo...')
                        except IndexError:
                            print (' ------- Que ya no quedan mas muyayo...!')
                            #lista = [K_UP, K_LEFT, K_DOWN, K_RIGHT]
                            lista = [K_UP, K_LEFT]
                            ch = random.choice(lista)
                            print('    Intento {}'.format(ch))
                            repetir = False
            print('    Escogemos: {}'.format(ch))
            return (ch, maximo, maximo_pos)
    
    
    
    
    