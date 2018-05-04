# -*- coding: utf-8 -*-   
'''
Created on 1 may. 2018

@author: miguelangel.garciar
'''
import sys
import dosmil.juego as g
from time import sleep

COM_HELP_1 = '-h'
COM_HELP_2 = '--help'
COM_SIZE_1 = '-s'
COM_SIZE_2 = '--size'
COM_MODO_1 = '-m'
COM_MODO_2 = '--mode'
COM_CELL_1 = '-c'
COM_CELL_2 = '--cell'

def uso_in_game():
    print("""
    Uso:
        {}        Mover hacia ARRIBA
        {}        Mover hacia la IZQUIERDA
        {}        Mover hacia ABAJO
        {}        Mover hacia la DERECHA
        {}        DESHACER ultimo movimiento
        {}        SALIR
    """.format(g.K_UP, g.K_LEFT, g.K_DOWN, g.K_RIGHT, g.K_UNDO, g.K_QUIT))

    

def bucle_principal_manual(game):
    continua = True
    while continua and game.acabado():
        game.imprimir()
        print('Escriba la siguiente orden (h para mostrar los posibles comandos)')
        
        game.mejor_jugada(0)
        
        try:
            while True:
                userInput = raw_input('> ')
                if len(userInput) == 1:
                    break
                print 'Escribe solo un caracter'
            ch = userInput.lower()
            if ch == 'h':
                uso_in_game()
            elif ch == g.K_QUIT:
                break
            elif ch == g.K_UNDO: # Esto habria que eliminarlo
                if game.deshacer():
                    print('Tablero deshecho al ultimo movimiento.')
                else:
                    print('No existe un tablero anterior.')
            elif ch == g.K_UP or ch == g.K_LEFT or ch == g.K_DOWN or ch == g.K_RIGHT:
                continua = game.mover(ch)
            else:
                print('No he reconocido el comando.')
                
        except ValueError:
            print('No he reconocido el comando.')
    
    if game.acabado():
        print('¡Ya no quedan mas movimientos! Fin de la partida')
    game.imprimir()
    print('Has finalizado con {} puntos tras {} movimientos.'.format(game.puntuacion, game.movimientos))
    sys.exit()
    
    '''
    # PRuebas
    game.nueva_casilla()
    game.nueva_casilla()
    game.nueva_casilla()
    game.imprimir()
    game.movimiento_izquierda(True)
    game.imprimir()
    sys.exit()
    
    '''

def usage():
    print("""
    Uso:
        {} | {}        Muestra las opciones en la llamada.
        {} | {}        Especifica el tama�o del tablero (entre 3 y 8). Por defecto: 4
        {} | {}        Modo de juego (m: manual, a: automatico)
        {} | {}        Tipo de casillas:
                            0: IMPOSIBLE!
                            1: normal, en base 2
                            2: en base 3
                            3: fibonacci
    """.format(COM_HELP_1, COM_HELP_2, COM_SIZE_1, COM_SIZE_2, COM_MODO_1, COM_MODO_2, COM_CELL_1, COM_CELL_2))



def bucle_principal_ia(game):
    #game.nueva_casilla()
    #game.nueva_casilla()
    while game.acabado():
        #game.imprimir()
        ch = game.mejor_jugada(5)[0]
        game.mover(ch)
        game.imprimir()
        sleep(0.5)
    
    print('¡Ya no quedan mas movimientos! Fin de la partida')
    game.imprimir()
    print('El ordenador ha conseguido {} puntos en {} movimientos.'.format(game.puntuacion, game.movimientos))
    sys.exit()


if __name__ == '__main__':
    # Tratamos los argumentos:
    tamanyo = 4 # 4 de tamaño por defecto
    nc = 1
    modo = 'a' # Modo manual por defecto
    argu = None
    del sys.argv[0] # Elimino la llamada al programa
    for el in sys.argv:
        if argu == None:
            if el == COM_SIZE_1 or el == COM_SIZE_2 or el == COM_MODO_1 or el == COM_MODO_2 or el == COM_CELL_1 or el == COM_CELL_2:
                argu = el
            else:
                argu = 'desconocido'
        else:
            if argu == COM_SIZE_1 or argu == COM_SIZE_2:
                if int(el) in g.Juego.TABLEROS:
                    tamanyo = int(el)
                    argu = None
                else:
                    print('Ese tamaño de tablero no es valido:')
                    usage()
                    sys.exit()
            elif argu == COM_MODO_1 or argu == COM_MODO_2:
                if el in ('m','a'):
                    modo = el
                    argu = None
                else:
                    print('Ese modo de juego no es valido:')
                    usage()
                    sys.exit()
            elif argu == COM_CELL_1 or argu == COM_CELL_2:
                try:
                    if int(el) >= 0 and int(el) < len(g.Juego.VALORES):
                        nc = int(el)
                        argu = None
                    else:
                        print('Ese tipo de celdas no es valido:')
                        usage()
                        sys.exit()
                except ValueError:
                    print('Ese tipo de celdas no es valido:')
                    usage()
                    sys.exit()
            else:
                print('Opcion no reconocida.')
                usage()
                sys.exit()
    # Creamos el juego:
    game = g.Juego(tamanyo)
    game.nueva_casilla()
    game.nueva_casilla()
    if modo == 'm':
        bucle_principal_manual(game)
    else:
        bucle_principal_ia(game)
        
        

        
        
        