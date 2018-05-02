# -*- coding: utf-8 -*-   
'''
Created on 1 may. 2018

@author: miguelangel.garciar
'''
import dosmil.juego
import sys
from dosmil.juego import Juego
from telnetlib import EL

COM_HELP_1 = '-h'
COM_HELP_2 = '--help'
COM_SIZE_1 = '-s'
COM_SIZE_2 = '--size'
COM_MODO_1 = '-m'
COM_MODO_2 = '--mode'

def usage():
    print("""
    Uso:
        {} | {}        Muestra las opciones en la llamada.
        {} | {}        Especifica el tama�o del tablero (entre 3 y 8). Por defecto: 4
        {} | {}        Modo de juego (m: manual, a: automatico)
    """.format(COM_HELP_1, COM_HELP_2, COM_SIZE_1, COM_SIZE_2, COM_MODO_1, COM_MODO_2))

if __name__ == '__main__':
    # Tratamos los argumentos:
    tamanyo = 4 # 4 de tamaño por defecto
    modo = 'm' # Modo manual por defecto
    argu = None
    del sys.argv[0] # Elimino la llamada al programa
    for el in sys.argv:
        if argu == None:
            if el == COM_SIZE_1 or el == COM_SIZE_2 or el == COM_MODO_1 or el == COM_MODO_2:
                argu = el
            else:
                argu = 'desconocido'
        else:
            if argu == COM_SIZE_1 or argu == COM_SIZE_2:
                if int(el) in Juego.TABLEROS:
                    tamanyo = int(el)
                else:
                    print('Ese tamaño de tablero no es valido:')
                    usage()
                    sys.exit()
            elif argu == COM_MODO_1 or argu == COM_MODO_2:
                if el in ('m','a'):
                    modo = el
                else:
                    print('Ese modo de juego no es valido:')
                    usage()
                    sys.exit()
            else:
                print('Opcion no reconocida.')
                usage()
                sys.exit()
    # Creamos el juego:
    game = Juego(tamanyo)
    if modo == 'm':
        # PRuebas
        game.nueva_casilla()
        game.nueva_casilla()
        game.nueva_casilla()
        game.imprimir()
        game.movimiento_izquierda(True)
        game.imprimir()
        sys.exit()
    else:
        sys.exit()