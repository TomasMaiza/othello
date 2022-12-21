#ifndef FUNCIONES_H 

#define FUNCIONES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* nombre, color;
    int cantidadDeFichas;
} Jugador;

typedef struct {
    char casillas[8][8], turnoSiguiente;
    int contorno[60][2], cantidadDefichasEnContorno;
} Tablero;

void inicializar_tablero(Tablero* tablero);
void tablero_inicial(Tablero* tablero);
void contorno_inicial(Tablero* tablero);
int leer_archivo_jugadas(FILE *jugadas, Jugador* jugadores, Tablero* tablero);
void leer_datos_jugador(FILE *jugadas, Jugador* jugadores);
char turno_inicial(FILE *jugadas);
int turno_inicial_valido(FILE *jugadas, char turno);
int leer_jugada(FILE *jugadas, char* jugada);
void jugada_a_coordenadas(char* jugada, int coordenadas[]);
int verificar_jugada(char* jugada, Jugador* jugadores, char turno, Tablero* tablero);
char cambiar_turno(char turno);
int fichas_a_voltear(Tablero* tablero, int coordenadas[], char turno, int (*listaDeFichas)[2]);
void desplazamientos(int casilla[], int i, int movimiento[]);
void sumar_desplazamiento(int casilla[], int movimiento[], int fila, int columna);
int casilla_fuera_de_rango(int casilla[]);
void array_append(int (*listaDeFichas)[2], int (*listaAuxiliar)[2], int tamanioListaDeFichas, int tamanioListaAuxiliar);
int hay_jugadas_validas(Tablero* tablero, char turno);
void modificar_tablero(Tablero* tablero, char turno, int casilla[], int (*listaDeFichas)[2], int tamanioListaDeFichas);
void modificar_casillas(Tablero* tablero, char turno, int casilla[], int (*listaDeFichas)[2], int tamanioListaDeFichas);
void modificar_contorno(Tablero* tablero, int casilla[]);
void eliminar_casilla(Tablero* tablero, int casilla[]);
int casillas_adyacentes_vacias(Tablero* tablero, int casilla[], int (*casillasAdyacentes)[2]);
int casilla_en_contorno(Tablero* tablero, int casilla[]);
void sumar_fichas(Jugador* jugadores, char turno, int fichasASumar);
void imprimir_tablero(Tablero* tablero);
int partida_finalizada(Tablero* tablero);
void mostrar_ganador(Jugador* jugadores);
void volcar_tablero_en_archivo(Tablero tablero, FILE* tableroFinal);
void liberar_memoria(Jugador* jugadores);

#endif