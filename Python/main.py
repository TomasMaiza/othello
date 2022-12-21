import sys, os, random

# DISEÑO DE DATOS #

'''
Tablero: lo represento como una lista de listas de string. Cada lista es una fila, y cada elemento de estas filas es una casilla.
Fichas: las represento con string. 'B' son las blancas, 'N' las negras y 'X' representa las casillas vacías.
Casillas: las jugadas se representan como strings que indican la casilla donde se quiere colocar una ficha, pero para acceder a las casillas en
el tablero utilizo una lista de dos enteros (o una tupla) que almacena la coordenada de la casilla (fila y columna del tablero).
Contorno: es un conjunto de tuplas de enteros que contiene todas las casillas donde podría colocarse una ficha.
'''

# tablero_vacio : none -> [[string]]
# tablero_vacio genera un tablero sin fichas.
def tablero_vacio():
    return [
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

# imprimir_tablero : [[string]] -> none
# imprimir_tablero toma un tablero y lo muestra en pantalla
def imprimir_tablero(tablero):
    bandera = 0
    nroFila = 1
    print("  +--------------------------+")
    for fila in tablero:
        for casilla in fila:
            if bandera == 0:
                print(nroFila, end="")
                print(" | ", end="")
            print(" " + casilla + " ", end="")
            bandera += 1
        print(" | ")
        nroFila += 1
        bandera = 0
    print("  +--------------------------+")
    print("     A  B  C  D  E  F  G  H")

# leer_tablero : file -> ([[string]], string)
# leer_tablero recibe el archivo con el tablero de entrada y retorna una tupla con el tablero y el turno que debe jugar a continuación.
def leer_tablero(tableroDeEntrada):
    tablero=tablero_vacio()
    i=0
    while(i<8):
        j=0
        casilla=tableroDeEntrada.read(1)
        while(casilla!='\n'):
            tablero[i][j]=casilla
            j+=1
            casilla=tableroDeEntrada.read(1)
        i+=1
    turno=tableroDeEntrada.read(1)
    return (tablero, turno)

# cambiar_turno : string -> string
# cambiar_turno cambia el color de la ficha
def cambiar_turno(turno):
    if turno == "N":
      return "B"
    return "N"

# casilla_fuera_de_rango : [int] -> boolean
# casilla_fuera_de_rango toma una lista de dos enteros y determina si sus coordenadas están fuera del rango de una casilla válida.
def casilla_fuera_de_rango(casilla):
    if casilla[0] not in range(0, 8) or casilla[1] not in range(0, 8):
        return True
    return False

# desplazamientos : int [int] -> [int]
# desplazamientos toma un entero y una casilla y retorna el desplazamiento correspondiente. 
def desplazamientos(i, casilla):
    desp={0:(-1, 0), 1:(-1, 1), 2:(0, 1), 3:(1,1), 4:(1, 0), 5:(1, -1), 6:(0, -1), 7:(-1, -1)}
    return [casilla[0]+desp[i][0], casilla[1]+desp[i][1]]

# fichas_a_voltear : [[string]], [int], string -> [[int]]
# fichas_a_voltear determina qué fichas deben voltearse al realizar una jugada en particular
def fichas_a_voltear(tablero, casilla, color):
    provisorio = []
    permanente = []
    colorOpuesto=cambiar_turno(color)
    anterior=-1
    i=0
    while i!=8:
        if anterior!=i:
            mov=desplazamientos(i, casilla)
        if casilla_fuera_de_rango(mov) or tablero[mov[0]][mov[1]]=='X': # la casilla se fue de rango o tiene una X?
            provisorio = []
            anterior=i
            i+=1
        elif tablero[mov[0]][mov[1]]==colorOpuesto: # hay una ficha de color opuesto?
            provisorio.append(mov)
            mov=desplazamientos(i, mov)
            anterior=i
        else: # la ficha es del mismo color que la inicial
            permanente += provisorio
            provisorio = []
            anterior=i
            i+=1
    return permanente

# jugada_a_coordenadas : string -> [int]
# jugada_a_coordenadas toma una jugada y devuelve sus coordenadas correspondientes (o vacío si la jugada leída no corresponde a una casilla).
def jugada_a_coordenadas(jugada):
    letra=jugada[0]
    num=jugada[1]
    if letra in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'} and num in {'1', '2', '3', '4', '5', '6', '7', '8'}:
        correspondencias = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        letra=correspondencias[letra]
        return [int(num)-1, letra]
    else:
        return []

# coordenadas_a_jugada : [int] -> string
# coordenadas_a_jugada toma una casilla del tablero y la convierte al formato de string LetraNúmero.
def coordenadas_a_jugada(casilla):
    if casilla==[]:
        return '\n'
    num=casilla[0]
    letra=casilla[1]
    correspondencias = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
    letra=correspondencias[letra]
    return letra+str(num+1)


# modificar_tablero : [[string]] [[int]] [int] string -> [[string]]
# modificar_tablero recibe un tablero, una lista de casillas a modificar, la casilla donde debe colocarse la nueva ficha y su color y retorna el tablero modificado
def modificar_tablero(tablero, casillas, ficha, color):
    tablero[ficha[0]][ficha[1]] = color
    for casilla in casillas:
        tablero[casilla[0]][casilla[1]] = color
    return tablero

# casillas_adyacentes_vacias : [[string]] [int] -> [[int]]
# casillas_adyacentes_vacias toma un tablero y una casilla y retorna una lista con aquellas casillas adyecentes a la pasada como parámetro que están vacías.
def casillas_adyacentes_vacias(tablero, casilla):
    listaDeCasillas=[]
    i=0
    while i != 8:
        mov=desplazamientos(i, casilla)
        if not casilla_fuera_de_rango(mov):
            if tablero[mov[0]][mov[1]] == "X":
                listaDeCasillas.append(mov)
        i+=1
    return listaDeCasillas

# hay_jugadas_validas : [[string]] string {(int, int)} -> boolean
# hay_jugadas_validas toma un tablero, el color del jugador y el contorno actual y verifica si hay movimientos válidos para cada ficha del conjunto contorno
def hay_jugadas_validas(tablero, color, contorno):
    for jugada in contorno:
        if fichas_a_voltear(tablero, [jugada[0], jugada[1]], color) != []:
            return True
    return False

# determinar_contorno : [[string]] -> {(int, int)}
# determinar_contorno toma un tablero y retorna un conjunto de tuplas que representan el contorno del tablero
def determinar_contorno(tablero):
    contorno=set()
    i=0
    j=0
    for fila in tablero:
        for casilla in fila:
            if(casilla!='X'):
                listaDeCasillas=casillas_adyacentes_vacias(tablero, [i, j])
                for lista in listaDeCasillas:
                    contorno = contorno.union({(lista[0], lista[1])})
            j+=1
        i+=1
        j=0
    return contorno

# verificar_jugada : [[string]] string string {(int, int)} -> boolean
# verificar_jugada toma el tablero, el turno y la jugada actuales y verifica que la misma sea válida. Si lo es, retorna True
def verificar_jugada(tablero, turno, jugada, contorno):
    saltoDeTurno=(jugada == '\n')
    if(saltoDeTurno and hay_jugadas_validas(tablero, turno, contorno)):
        print("Movimiento invalido. No puedes se puede saltar un turno si hay jugadas validas.")
        return False
    elif len(jugada)!=2 and not saltoDeTurno:
        print("Movimiento invalido. La jugada debe contener unicamente dos caracteres.")
        return False
    elif not saltoDeTurno:
        casilla=jugada_a_coordenadas(jugada)
        if casilla==[]:
            print("Movimiento invalido. Se ingreso una casilla inexistente")
            return False
        else:
            darVuelta = fichas_a_voltear(tablero, casilla, turno)
            if tablero[casilla[0]][casilla[1]]!='X' or darVuelta==[]:
                print("Movimiento invalido. No se puede colocar una ficha en esa casilla.")
                return False
    return True

# limpiar_consola : [[string]] string {(int, int)} -> none
# limpiar_consola limpia la consola.
def limpiar_consola():
    os.system("pause")
    os.system("cls")

# modificar_tablero : [[string]] string [int] -> [[string]]
# modificar_tablero actualiza el tablero tras realizar una jugada.
def modificar_tablero(tablero, turno, casilla):
    tablero[casilla[0]][casilla[1]]=turno
    darVuelta = fichas_a_voltear(tablero, casilla, turno)
    for ficha in darVuelta:
        tablero[ficha[0]][ficha[1]]=turno
    return tablero

# modificar_contorno : [[string]] {(int, int)} [int] -> {(int, int)}
# modificar_contorno actualiza el contorno tras realizar una jugada.
def modificar_contorno(tablero, contorno, casilla):
    listaDeCasillas = casillas_adyacentes_vacias(tablero, casilla)
    casillasAdyacentes=[]
    for casillaAdyacenteVacia in listaDeCasillas:
        casillasAdyacentes.append((casillaAdyacenteVacia[0], casillaAdyacenteVacia[1]))
    contorno=contorno.union(casillasAdyacentes)
    contorno.remove((casilla[0], casilla[1]))
    return contorno

# jugar_jugador : [[string]] string {(int, int)} -> [int]
# jugar_jugador toma el tablero, el color del jugador y el contorno y permite al jugador ingresar una jugada.
def jugar_jugador(tablero, turno, contorno):
    jugada = input("Ingrese su jugada: ")
    if jugada=="":
        jugada="\n"
    if not verificar_jugada(tablero, turno, jugada, contorno):
        print("A continuacion debera reingresar su jugada.")
        return jugar_jugador(tablero, turno, contorno)
    elif jugada!='\n':
        casilla=jugada_a_coordenadas(jugada)
        return casilla
    else:
        return []

# jugar_nivel0 : [[string]] string {(int, int)} -> [int]
# jugar_nivel0 toma el tablero y el turno actual permite realizar jugadas en nivel 0.
def jugar_nivel0(tablero, turno, contorno):
    jugadasPosibles=[]
    for coordenada in contorno:
        casilla=[coordenada[0], coordenada[1]]
        if fichas_a_voltear(tablero, casilla, turno)!=[]:
            jugadasPosibles.append(casilla)
    if jugadasPosibles!=[]:
        jugada=random.choice(jugadasPosibles)
        return jugada
    else:
        return []

# jugar_nivel1 : [[string]] string {(int, int)} -> [int]
# jugar_nivel1 toma el tablero y el turno actual permite realizar jugadas en nivel 1.
def jugar_nivel1(tablero, turno, contorno):
    maximo=0
    jugada=[]
    for coordenada in contorno:
        casilla=[coordenada[0], coordenada[1]]
        cantidadDeFichasVolteadas=len(fichas_a_voltear(tablero, casilla, turno))
        if cantidadDeFichasVolteadas>maximo:
            jugada=casilla
            maximo=cantidadDeFichasVolteadas
    return jugada

# jugar_programa : [[string]] string {(int, int)} int -> [int]
# jugar_programa permite al programa realizar una jugada según el nivel seleccionado.
def jugar_programa(tablero, turno, contorno, nivel):
    if nivel==0:
        return jugar_nivel0(tablero, turno, contorno)
    else:
        return jugar_nivel1(tablero, turno, contorno)

# imprimir_mensaje : boolean string string -> none
# imprimir_mensaje según el jugador que haya puesto una ficha, esta función imprime una descripción de la jugada realizada.
def imprimir_mensaje(turnoJugador, jugada, turno):
    if(turnoJugador):
        if jugada!='\n':
            print("Colocaste una ficha " + turno + " en la casilla " + jugada)
        else:
            print("Saltaste tu turno")
    else:
        if jugada!='\n':
            print("El programa colocó una ficha " + turno + " en la casilla " + jugada)
        else:
            print("El programa saltó su turno")

# partida_finalizada : [[string]] {(int, int)} -> boolean
# partida_finalizada determina si aún hay movimientos disponibles en el tablero.
def partida_finalizada(tablero, contorno):
    return not(hay_jugadas_validas(tablero, 'B', contorno) or hay_jugadas_validas(tablero, 'N', contorno))

# contar_fichas : [[string]] -> diccionario
# contar_fichas toma el tablero y retorna un diccionario que almacena la cantidad de fichas colocadas de cada color.
def contar_fichas(tablero):
    fichas={'N':0, 'B':0}
    for fila in tablero:
        for casilla in fila:
            if casilla=='N':
                fichas['N']+=1
            elif casilla=='B':
                fichas['B']+=1
    return fichas

# determinar_ganador : [[string]] string -> none 
# determinar_ganador recibe el tablero final y determina cuántas fichas puso cada jugador. Finalmente muestra quién ganó o si empataron.
def determinar_ganador(tablero, colorJugador):
    fichas=contar_fichas(tablero)
    cantidadNegras = fichas['N']
    cantidadBlancas = fichas['B']
    print("N: " + str(cantidadNegras) + "\nB: " + str(cantidadBlancas))
    if cantidadBlancas==cantidadNegras:
        print("Empate!!!")
    elif (cantidadNegras>cantidadBlancas and colorJugador=='N') or (cantidadBlancas>cantidadNegras and colorJugador=='B'):
        print("Felicitaciones!!! Has ganado la partida")
    else:
        print("El programa ha ganado la partida!!!")

# jugar : [[string]] int string string -> none
# jugar toma los datos requeridos para llevar a cabo la partida hasta completarse.
def jugar(tablero, nivel, turno, colorJugador):
    contorno=determinar_contorno(tablero)
    print("TABLERO INICIAL")
    imprimir_tablero(tablero)
    limpiar_consola()
    while(not partida_finalizada(tablero, contorno)):
        imprimir_tablero(tablero)
        turnoJugador=turno==colorJugador
        if(turnoJugador):
            casilla=jugar_jugador(tablero, turno, contorno)
        else:
            casilla=jugar_programa(tablero, turno, contorno, nivel)
        if casilla!=[]:
            tablero=modificar_tablero(tablero, turno, casilla)
            contorno=modificar_contorno(tablero, contorno, casilla)
        imprimir_tablero(tablero)
        jugada=coordenadas_a_jugada(casilla)
        imprimir_mensaje(turnoJugador, jugada, turno)
        turno=cambiar_turno(turno)
        limpiar_consola()
    print("TABLERO FINAL")
    imprimir_tablero(tablero)
    determinar_ganador(tablero, colorJugador)
    

# main : none -> none
# main se ejecuta al correr el archivo
def main():
    nombreArchivoDeEntrada=sys.argv[1]
    colorJugador=sys.argv[2] 
    if sys.argv[3] in {'0', '1'}:
        nivel=int(sys.argv[3])
    else:
        print("Se ingresó un nivel no disponible.")
        return
    try:
        tableroDeEntrada=open("../C/"+nombreArchivoDeEntrada, 'r')
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return
    (tablero, turno)=leer_tablero(tableroDeEntrada)
    os.system("cls")
    jugar(tablero, nivel, turno, colorJugador)
    
if __name__ == "__main__":
    main()