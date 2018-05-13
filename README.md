# 2048

El famoso juego de Gabriele Cirulli desarrollado en Python para CLI.

## Introducción

Este juego tiene diferentes modos, en los que se encuentran diferentes tamaños del tablero (de 3 a 8) y diferentes valores de casillas (exponentes de 2, de 3, suma y Fibonacci). Además, se puede jugar de forma manual o dejar que el ordenador juegue solo.

## Motivación

¿Por qué no? Intentando soltarme con Python y aprovechando para repasar un poco de inteligencia artificial.

## Instalación

Para poder usarlo, debemos tener un equipo con Python instalado. Una vez que lo tengamos, descargamos los ficheros de la carpeta "dosmil" y ejecutamos el fichero 2048.py:

```
python 2048.py
```

Existen modificadores para cambiar el tipo de juego (también se pueden ver poniendo -h o --help en la llamada al programa):

```
python 2048.py -s 5
# -s (o --size) Cambia el tamaño del tablero (de 3 a 8)
```

```
python 2048.py -m a
# -m (o --mode) indica el modo de juego (m: manual, a: automático)
```

**⚠️ NO DISPONIBLE en este momento.**
```
python 2048.py -c 3
# -c (o --cell) Cambia el tipo de celdas. (0: IMPOSIBLE, 1: juego normal, 2: exponentes de 3, 3: suma de elementos, 4: Fibonacci)
```

Se pueden unir cualquier modificador para cargar cualquier tipo de juego:
```
python 2048.py -s 7 -c 2 -m a
```

### Uso manual

Durante la partida, se pide al usuario por teclado que introduzca una tecla pudiendo ser cualquiera de las siguientes:

```
h:  Mostrar los comandos de ayuda en el juego (estas órdenes de aquí abajo)
w:  Mover hacia ARRIBA
a:  Mover hacia la IZQUIERDA
s:  Mover hacia ABAJO
d:  Mover hacia la DERECHA
u:  DESHACER ultimo movimiento
q:  SALIR
```

## Capturas

Modo manual 👤:

```
---------------------------------------------------------------------
 * Puntuacion: 328 | Movimientos: 51

    32        -         -         2     

    32        8         2         -     

    16        4         -         -     

    2         4         2         4     

---------------------------------------------------------------------
Escriba la siguiente orden (h para mostrar los posibles comandos)
> w
---------------------------------------------------------------------
 * Puntuacion: 404 | Movimientos: 52

    64        8         4         2     

    16        8         -         4     

    2         -         -         -     

    -         -         2         -     

---------------------------------------------------------------------
```

Modo automatico 💻:

```
---------------------------------------------------------------------
 * Puntuacion: 1040 | Movimientos: 118

    2         8         16        2     

    4         64        8         64    

    2         64        4         2     

    4         4         -         -     

---------------------------------------------------------------------
 * He tardado 102 milisegundos en pensar la jugada.
---------------------------------------------------------------------
 * Puntuacion: 1168 | Movimientos: 119

    2         -         2         -     

    4         8         16        2     

    2        128        8         64    

    4         4         4         2     

---------------------------------------------------------------------
```

Hasta el día 5/5/2018, el record personal del ordenador 🏆 ha sido:

```
---------------------------------------------------------------------
 * Puntuacion: 6360 | Movimientos: 441

    2         16        4         2     

    64        4        512        32    

    4        256        8         4     

    2         8         4         2     

---------------------------------------------------------------------
El ordenador ha conseguido 6360 puntos en 441 movimientos.
```

## Próximas funcionalidades

* Optimizar IA. Cambiar la estrategia para que realice un juego con la mejor táctica.

* Reestructuración de código, comentarios, etc.

* ¿Interfaz gráfica? Pilla un poco lejos ahora...

## Contacto

Correo electrónico: miguelangel.garciar@edu.uah.es

LinkedIn: Miguel Romeral (https://www.linkedin.com/in/miguelromeral/)

Twitter: @MiguelRomeral (https://twitter.com/MiguelRomeral)

## Licencia

Licencia Pública General GNU 3.0
