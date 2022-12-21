#include "main.h"

/*
A lo largo del programa representé los datos de las siguientes formas:

Jugadores: con una estructura Jugador que contiene su nombre, su color de fichas y su cantidad de fichas en el tablero.
Jugadas: puntero a un archivo de texto.
Tablero: con una estructura Tablero que contiene un array de arrays (el tablero en sí mismo) y el contorno (casillas en las que se puede color fichas en el próximo turno).
Fichas: con un char. 'B' es una ficha blanca, 'N' una negra y 'X' representa que la casilla está vacía.
Casillas: cadenas de dos caracteres. El primero indica la columna y el segundo la fila.
*/

int main(int argc, char** argv) {
    char* nombreArchivoJugadas=argv[1], *nombreArchivoTablero=argv[2];
    Tablero tablero;
    inicializar_tablero(&tablero);
    Jugador jugadores[2];
    jugadores[0].cantidadDeFichas=2;
    jugadores[1].cantidadDeFichas=2;
    FILE *jugadas=fopen(nombreArchivoJugadas, "r"), *tableroFinal=fopen(nombreArchivoTablero, "w");
    int partidaFinalizada=leer_archivo_jugadas(jugadas, jugadores, &tablero);
    imprimir_tablero(&tablero);
    if(partidaFinalizada==1)
        mostrar_ganador(jugadores);
    else {
        printf("\nPartida inconclusa\n");
        volcar_tablero_en_archivo(tablero, tableroFinal);
    }
    liberar_memoria(jugadores);
    fclose(jugadas);
    fclose(tableroFinal);
    return 0;
}
