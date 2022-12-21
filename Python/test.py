from main import *

def test_tablero_vacio():
    assert tablero_vacio() == [
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

def test_leer_tablero():
    t2=open("../Archivos de prueba/tablero2.txt", 'r')
    t3=open("../Archivos de prueba/tablero3.txt", 'r')
    t4=open("../Archivos de prueba/tablero4.txt", 'r')
    t6=open("../Archivos de prueba/tablero6.txt", 'r')
    t7=open("../Archivos de prueba/tablero7.txt", 'r')
    t9=open("../Archivos de prueba/tablero9.txt", 'r')
    assert leer_tablero(t2) == ([
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'N', 'X', 'X'],
        ['X', 'X', 'B', 'B', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'N', 'X', 'X'],
        ['X', 'X', 'N', 'B', 'B', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['N', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ], 'B')
    assert leer_tablero(t3) == ([
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'N', 'X', 'X'],
        ['X', 'X', 'B', 'B', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'N', 'X', 'X'],
        ['X', 'X', 'N', 'B', 'B', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['N', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ], 'B')
    assert leer_tablero(t4) == ([
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'N', 'X', 'X'],
        ['X', 'X', 'B', 'B', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['X', 'X', 'N', 'B', 'B', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['N', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ], 'N')
    assert leer_tablero(t6) == ([
        ['N', 'X', 'B', 'X', 'X', 'N', 'X', 'X'],
        ['X', 'N', 'B', 'B', 'N', 'N', 'X', 'X'],
        ['B', 'B', 'N', 'N', 'B', 'N', 'X', 'X'],
        ['B', 'X', 'N', 'B', 'B', 'N', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['B', 'N', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['N', 'B', 'B', 'N', 'X', 'N', 'X', 'X']
    ], 'B')
    assert leer_tablero(t7) == ([
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'B', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ], 'N')
    assert leer_tablero(t9) == ([
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ], 'B')
    t2.close()
    t3.close()
    t4.close()
    t6.close()
    t7.close()
    t9.close()

def test_cambiar_turno():
    assert cambiar_turno("N") == "B"
    assert cambiar_turno("B") == "N"

def test_casilla_fuera_de_rango():
    assert casilla_fuera_de_rango([0, 3])==False
    assert casilla_fuera_de_rango([5, 7])==False
    assert casilla_fuera_de_rango([5, 2])==False
    assert casilla_fuera_de_rango([8, 3])==True
    assert casilla_fuera_de_rango([2, -1])==True

def test_desplazamientos():
    assert desplazamientos(0, [3, 5])==[2, 5]
    assert desplazamientos(5, [3, 5])==[4, 4]
    assert desplazamientos(6, [0, 3])==[0, 2]
    assert desplazamientos(7, [7, 7])==[6, 6]

def test_fichas_a_voltear():
    tableroInicial =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    t = [
        ['N', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'X', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'B', 'X', 'B', 'N', 'X'],
        ['X', 'B', 'X', 'B', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'N', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'B', 'X', 'B'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'B', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'N']
    ]
    assert fichas_a_voltear(tableroInicial, [3, 5], 'B') == [[3, 4]]
    assert fichas_a_voltear(tableroInicial, [3, 5], 'N') == []
    assert fichas_a_voltear(tableroInicial, [5, 4], 'N') == [[4, 4]]
    assert fichas_a_voltear(t, [0, 3], 'N') == [[1, 3], [2, 3], [3, 3]]
    assert fichas_a_voltear(t, [2, 2], 'N') == [[3, 3], [4, 4], [5, 5], [6, 6]]
    assert fichas_a_voltear(t, [1, 6], 'B') == []

def test_jugada_a_coordenadas():
    assert jugada_a_coordenadas('J3')==[]
    assert jugada_a_coordenadas('1A')==[]
    assert jugada_a_coordenadas('A5')==[4, 0]
    assert jugada_a_coordenadas('C6')==[5, 2]

def test_coordenadas_a_jugada():
    assert coordenadas_a_jugada([4, 0])=="A5"
    assert coordenadas_a_jugada([5, 2])=="C6"
    assert coordenadas_a_jugada([0, 0])=="A1"
    assert coordenadas_a_jugada([7, 7])=="H8"
    assert coordenadas_a_jugada([])=="\n"

def test_modificar_tablero():
    tableroInicial =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    t = [
        ['N', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'X', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'B', 'X', 'B', 'N', 'X'],
        ['X', 'B', 'X', 'B', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'N', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'B', 'X', 'B'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'B', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'N']
    ]
    assert modificar_tablero(tableroInicial, [[3, 4]], [3, 5], 'B') == [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'B', 'B', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    assert modificar_tablero(t, [[1, 3], [2, 3], [3, 3]], [0,3], 'N') == [
        ['N', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'N', 'X', 'B', 'N', 'X'],
        ['X', 'B', 'X', 'N', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'N', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'B', 'X', 'B'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'B', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'N']
    ]

def test_casillas_adyacentes_vacias():
    tableroInicial =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    t = [
        ['N', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'X', 'X', 'X', 'X'],
        ['X', 'N', 'X', 'B', 'X', 'B', 'N', 'X'],
        ['X', 'B', 'X', 'B', 'N', 'N', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'N', 'X', 'X'],
        ['X', 'B', 'X', 'X', 'X', 'B', 'X', 'B'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'B', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'N']
    ]
    assert casillas_adyacentes_vacias(tableroInicial, [2, 3]) == [[1, 3], [1, 4], [2, 4], [3, 2], [2, 2], [1, 2]]
    assert casillas_adyacentes_vacias(tableroInicial, [3, 4]) == [[2, 4], [2, 5], [3, 5], [4, 5], [2, 3]]
    assert casillas_adyacentes_vacias(t, [3, 4]) == [[2, 4]]
    assert casillas_adyacentes_vacias(t, [7, 7]) == [[6, 7]]

def test_hay_jugadas_validas():
    tableroInicial =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    t1 = [
        ['X', 'X', 'X', 'X', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'B', 'B', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'B', 'X', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'N'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    contornoInicial = {(3,2), (4,2), (5,2), (5,3), (5,4), (4,5), (3,5), (2,5), (2,4), (2,3), (2,2), (5,5)}
    contornot1 = {(1, 0), (1, 1), (1, 2), (1, 3), (0, 3), (0, 5), (0, 6), (1, 6), (1, 7), (5, 7), (5, 6), (4, 6), (3, 6), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 0)}
    assert hay_jugadas_validas(tableroInicial, "B", contornoInicial) == True
    assert hay_jugadas_validas(t1, "N", contornot1) == False
    assert hay_jugadas_validas(t1, "B", contornot1) == False

def test_determinar_contorno():
    tableroInicial =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    t1 = [
        ['X', 'X', 'X', 'X', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'B', 'B', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'B', 'X', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'N'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    assert determinar_contorno(tableroInicial) == {(3,2), (4,2), (5,2), (5,3), (5,4), (4,5), (3,5), (2,5), (2,4), (2,3), (2,2), (5,5)}
    assert determinar_contorno(t1) == {(1, 0), (1, 1), (1, 2), (1, 3), (0, 3), (0, 5), (0, 6), (1, 6), (1, 7), (5, 7), (5, 6), (4, 6), (3, 6), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 0)}

def test_verificar_jugada():
    tableroInicial =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    t1 = [
        ['X', 'X', 'X', 'X', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'B', 'B', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'B', 'X', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'N'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    contornoInicial = {(3,2), (4,2), (5,2), (5,3), (5,4), (4,5), (3,5), (2,5), (2,4), (2,3), (2,2), (5,5)}
    contornot1 = {(1, 0), (1, 1), (1, 2), (1, 3), (0, 3), (0, 5), (0, 6), (1, 6), (1, 7), (5, 7), (5, 6), (4, 6), (3, 6), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 0)}
    assert verificar_jugada(tableroInicial, 'B', "C3", contornoInicial)==False
    assert verificar_jugada(tableroInicial, 'N', "D3", contornoInicial)==True
    assert verificar_jugada(tableroInicial, 'N', "\n", contornoInicial)==False
    assert verificar_jugada(t1, 'B', "D5", contornot1)==False
    assert verificar_jugada(t1, 'B', "D53", contornot1)==False
    assert verificar_jugada(t1, 'B', "K8", contornot1)==False
    assert verificar_jugada(t1, 'N', "\n", contornot1)==True

def test_modificar_tablero():
    tableroInicial1 =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    tableroInicial2 =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    assert modificar_tablero(tableroInicial1, 'N', [2, 3])==[
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    assert modificar_tablero(tableroInicial2, 'B', [5, 3])==[
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'B', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

def test_modificar_contorno():
    tablero1 =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    contornoInicial = {(3,2), (4,2), (5,2), (5,3), (5,4), (4,5), (3,5), (2,5), (2,4), (2,3), (2,2), (5,5)}
    assert modificar_contorno(tablero1, contornoInicial, [2, 3])== {(1, 2), (1, 3), (1, 4), (3,2), (4,2), (5,2), (5,3), (5,4), (4,5), (3,5), (2,5), (2,4), (2,2), (5,5)}

def test_partida_finalizada():
    tablero1 =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    tablero2 = [
        ['X', 'X', 'X', 'X', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'B', 'B', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'B', 'X', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'N'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    contorno1={(1, 2), (1, 3), (1, 4), (3,2), (4,2), (5,2), (5,3), (5,4), (4,5), (3,5), (2,5), (2,4), (2,2), (5,5)}
    contorno2 = {(1, 0), (1, 1), (1, 2), (1, 3), (0, 3), (0, 5), (0, 6), (1, 6), (1, 7), (5, 7), (5, 6), (4, 6), (3, 6), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 0)}
    assert partida_finalizada(tablero1, contorno1)==False
    assert partida_finalizada(tablero2, contorno2)==True

def test_contar_fichas():
    tablero1 =  [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    tablero2 = [
        ['X', 'X', 'X', 'X', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'B', 'B', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'B', 'X', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'N'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    assert contar_fichas(tablero1)=={'N':4, 'B':1}
    assert contar_fichas(tablero2)=={'N':3, 'B':17}

def test_jugar_nivel1():
    tablero=[
        ['N', 'X', 'B', 'X', 'X', 'N', 'X', 'X'],
        ['X', 'N', 'B', 'B', 'N', 'N', 'X', 'X'],
        ['B', 'B', 'N', 'N', 'B', 'N', 'X', 'X'],
        ['B', 'X', 'N', 'B', 'B', 'N', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['B', 'N', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'N', 'X', 'X'],
        ['N', 'B', 'B', 'N', 'X', 'N', 'X', 'X']
    ]
    tablero2 = [
        ['X', 'X', 'X', 'X', 'B', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'B', 'B', 'X', 'X'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'B', 'X', 'N'],
        ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'N'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    contorno={(0,1),(0,3),(0,4),(0,6),(0,7),(1,0),(1,6),(1,7),(2,6),(2,7),(3,1),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7),(6,6),(6,7),(7,4),(7,6),(7,7)}
    contorno2={(0,3),(0,5),(0,6),(1,0),(1,1),(1,2),(1,3),(1,6),(1,7),(3,0),(3,1),(3,6),(4,1),(4,5),(4,6),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7)}
    assert jugar_nivel1(tablero, 'N', contorno)==[7, 4]or[1,0]
    assert jugar_nivel1(tablero2, 'B', contorno2)==[]
    assert jugar_nivel1(tablero2, 'N', contorno2)==[]