#include "funciones.h"

// inicializar_tablero : Tablero* -> void
// inicializar_tablero toma la dirección de memoria de un tablero e inicializa sus casillas y su contorno.
void inicializar_tablero(Tablero* tablero) {
    tablero_inicial(tablero);
    contorno_inicial(tablero);
}

// tablero_inicial : Tablero* -> void
// tablero_inicial almacena las fichas correspondientes al tablero inicial en la dirección de memoria del tablero.
void tablero_inicial(Tablero* tablero) {
    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            tablero->casillas[i][j] = 'X';
        }
    }
    tablero->casillas[3][3]='B';
    tablero->casillas[3][4]='N';
    tablero->casillas[4][3]='N';
    tablero->casillas[4][4]='B';
}

// contorno_inicial : Tablero* -> void
// contorno_inicial almacena las casillas correspondientes al contorno del tablero inicial en la dirección de memoria del tablero.
void contorno_inicial(Tablero* tablero) {
    tablero->contorno[0][0]=2;
    tablero->contorno[0][1]=2;
    tablero->contorno[1][0]=2;
    tablero->contorno[1][1]=3;
    tablero->contorno[2][0]=2;
    tablero->contorno[2][1]=4;
    tablero->contorno[3][0]=2;
    tablero->contorno[3][1]=5;
    tablero->contorno[4][0]=3;
    tablero->contorno[4][1]=2;
    tablero->contorno[5][0]=3;
    tablero->contorno[5][1]=5;
    tablero->contorno[6][0]=4;
    tablero->contorno[6][1]=2;
    tablero->contorno[7][0]=4;
    tablero->contorno[7][1]=5;
    tablero->contorno[8][0]=5;
    tablero->contorno[8][1]=2;
    tablero->contorno[9][0]=5;
    tablero->contorno[9][1]=3;
    tablero->contorno[10][0]=5;
    tablero->contorno[10][1]=4;
    tablero->contorno[11][0]=5;
    tablero->contorno[11][1]=5;
    tablero->cantidadDefichasEnContorno=11;
}

// leer_archivo_jugadas : FILE* Jugador* Tablero* -> int
// leer_archivo_jugadas toma el archivo de jugadas y un array de Jugadores y procesa la información del archivo. Retorna 1 si la partida finalizó
//ó 0 si hubo jugadas inválidas o la partida quedó inconclusa.
int leer_archivo_jugadas(FILE *jugadas, Jugador* jugadores, Tablero* tablero) {
    int terminarBucle=-1;
    char turno, *jugada;
    leer_datos_jugador(jugadas, &(jugadores[0]));
    leer_datos_jugador(jugadas, &(jugadores[1]));
    turno=turno_inicial(jugadas);
    if(turno_inicial_valido(jugadas, turno) == 0) {
        printf("Error al leer el color inicial. El formato del archivo es incorrecto.\n");
        return 0;
    }
    while(terminarBucle==-1) {
        if(leer_jugada(jugadas, jugada)==0) 
            terminarBucle=1;
        else if(verificar_jugada(jugada, jugadores, turno, tablero)==0)
            terminarBucle++;
        if(terminarBucle==-1)
            turno=cambiar_turno(turno);
    }
    tablero->turnoSiguiente=turno;
    if(terminarBucle==1 && partida_finalizada(tablero)==1) {
        return 1;
    }
    return 0;
}

// leer_datos_jugador : FILE* Jugador* -> void
// leer_datos_jugador toma un archivo de jugadas y puntero a una estructura jugador y almacena en su direccion de memoria el nombre y color del jugador leidos en el archivo. 
void leer_datos_jugador(FILE *jugadas, Jugador* jugador) {
    char nombre[30];
    fscanf(jugadas, "%[^,]", nombre);
    jugador->nombre = malloc(sizeof(char)*(strlen(nombre)+1));
    strcpy(jugador->nombre, nombre);
    fgetc(jugadas);
    jugador->color = fgetc(jugadas);
    fgetc(jugadas);
}

// turno_inicial : FILE* -> char
// turno_inicial toma el archivo de jugadas y retorna el turno inicial (tercera linea del archivo).
char turno_inicial(FILE* jugadas) {
    char turno;
    turno=fgetc(jugadas);
    return turno;
}

// turno_inicial_valido : FILE* char -> int
// turno_inicial_valido toma el archivo de jugadas y el turno inicial y comprueba que el formato del archivo sea válido. Si lo es, retorna 1. Si el turno es distinto de B o N, retorna 0.
int turno_inicial_valido(FILE *jugadas, char turno) {
    char siguienteCaracter=getc(jugadas);
    if(siguienteCaracter=='\n' && (turno=='B' || turno=='N'))
        return 1;
    return 0;
}

// leer_jugada : FILE* char* -> int
// leer_jugada lee una jugada del archivo de jugadas. Retorna 1 si el archivo aún no se termina ó 0 si se intentó leer más allá del EOF.
int leer_jugada(FILE* jugadas, char* jugada) {
    if(!feof(jugadas)) {
        fgets(jugada, 3, jugadas);
        if(strcmp(jugada, "\n")!=0) {
            jugada[2]=fgetc(jugadas);
            if(jugada[2]==EOF) {
                jugada[2]='\n';
            }
            jugada[3]='\0';
        }
        return 1;
    }
    return 0;
}

// jugada_a_coordenadas : char* int* -> void
// jugada_a_coordenadas toma una jugada (en formato LetraFila) y lo convierte en coordenadas (NumfilaNumcolumna) para acceder al tablero. 
void jugada_a_coordenadas(char* jugada, int coordenadas[]) {
    coordenadas[0]=jugada[1]-'1';
    coordenadas[1]=(int)jugada[0]-65;
}

// verificar_jugada : char* Jugador* char Tablero* -> int
// verificar_jugada recibe una jugada y retorna 1 si la jugada es valida o 0 si hubo algun error.
int verificar_jugada(char* jugada, Jugador* jugadores, char turno, Tablero* tablero) {
    int largoJugada=strlen(jugada), jugadaVacia=strcmp(jugada, "\n");
    if(jugadaVacia==0 && hay_jugadas_validas(tablero, turno)==1) {
        printf("El jugador de fichas %c intento saltar un turno cuando tenia movimientos validos disponibles.\n", turno);
        return 0;
    }
    else if(jugada[largoJugada-1]!='\n') {
        printf("Formato de jugada invalido, la jugada debe tener dos caracteres.\n");
        return 0;
    }
    else if(jugadaVacia!=0){
        int coordenadas[2];
        jugada_a_coordenadas(jugada, coordenadas);
        if(casilla_fuera_de_rango(coordenadas)==1) {
            printf("Se intento colocar una ficha en una casilla inexistente.\n");
            return 0;
        }
        else {
            int listasDeFichas[60][2], tamanioListaDeFichas;
            tamanioListaDeFichas=fichas_a_voltear(tablero, coordenadas, turno, listasDeFichas);
            if(tamanioListaDeFichas==0 || tablero->casillas[coordenadas[0]][coordenadas[1]]!='X') { // si no hay fichas que voltear o la casilla está ocupada entonces la jugada es inválida.
                printf("Jugada invalida. El jugador de fichas %c intento colocar una ficha en la casilla %s\n", turno, jugada);
                return 0;
            }
            else {
                modificar_tablero(tablero, turno, coordenadas, listasDeFichas, tamanioListaDeFichas);
                sumar_fichas(jugadores, turno, tamanioListaDeFichas+1);
            }
        }
    }
    return 1;
}

// cambiar_turno : char -> char
// cambiar_turno toma un caracter que indica un color y devuelve el opuesto.
char cambiar_turno(char turno) {
    if(turno=='B')
        return 'N';
    return 'B';
}

// fichas_a_voltear : Tablero* int* char int** -> int
// fichas_a_voltear toma un puntero al tablero, coordenadas de una casilla, el color del jugador y un array vacio donde colocará las casillas donde hay fichas que se deben voltear al colocar
//una ficha del color dado en las coordenadas dadas. Retorna la cantidad de fichas que se voltean.
int fichas_a_voltear(Tablero* tablero, int casilla[], char turno, int (*listaDeFichas)[2]) {
    int listaAuxiliar[60][2], tamanioListaAuxiliar=0, movimiento[2], i=0, tamanioListaDeFichas=0, anterior=-1; // anterior es un auxiliar para determinar cuándo debe desplazarse desde la casilla.
    char colorOpuesto=cambiar_turno(turno);
    while(i<8) {
        if(anterior!=i)
            desplazamientos(casilla, i, movimiento);
        if(casilla_fuera_de_rango(movimiento)==1 || tablero->casillas[movimiento[0]][movimiento[1]]=='X') {  // la casilla se fue de rango o tiene una X?
            tamanioListaAuxiliar=0;
            anterior=i;
            i++;
        }
        else if(tablero->casillas[movimiento[0]][movimiento[1]]==colorOpuesto) { // hay una ficha de color opuesto?
            listaAuxiliar[tamanioListaAuxiliar][0]=movimiento[0];
            listaAuxiliar[tamanioListaAuxiliar][1]=movimiento[1];
            tamanioListaAuxiliar++;
            desplazamientos(movimiento, i, movimiento);
            anterior=i;
        }
        else { // la ficha es del mismo color que la inicial?
            array_append(listaDeFichas, listaAuxiliar, tamanioListaDeFichas, tamanioListaAuxiliar);
            tamanioListaDeFichas+=tamanioListaAuxiliar;
            tamanioListaAuxiliar=0;
            anterior=i;
            i++;
        }
    }
    return tamanioListaDeFichas;
}

// desplazamientos : int* int int* -> void
// desplazamientos toma un array de coordenadas de una casilla y el número correspondiente a la iteración de fichas_a_voltear y realiza el desplazamiento correspondiente en alguna dirección.
void desplazamientos(int casilla[], int i, int movimiento[]) {
    switch(i) {
        case 0: sumar_desplazamiento(casilla, movimiento, -1, 0); break;
        case 1: sumar_desplazamiento(casilla, movimiento, -1, 1); break;
        case 2: sumar_desplazamiento(casilla, movimiento, 0, 1); break;
        case 3: sumar_desplazamiento(casilla, movimiento, 1, 1); break;
        case 4: sumar_desplazamiento(casilla, movimiento, 1, 0); break;
        case 5: sumar_desplazamiento(casilla, movimiento, 1, -1); break;
        case 6: sumar_desplazamiento(casilla, movimiento, 0, -1); break;
        case 7: sumar_desplazamiento(casilla, movimiento, -1, -1); break;
    }
}

// sumar_desplazamiento : int* int* int int -> void
// sumar_desplazamiento toma una casilla y le suma una cantidad de casillas y una cantidad de columnas dadas.
void sumar_desplazamiento(int casilla[], int movimiento[], int fila, int columna) {
    movimiento[0]=casilla[0]+fila;
    movimiento[1]=casilla[1]+columna;
}

// casilla_fuera_de_rango : int* -> int
// casilla_fuera_de_rango retorna 1 si la casilla está fuera de rango ó 0 si es una casilla existente. 
int casilla_fuera_de_rango(int casilla[]) {
    for(int i=0; i<2; i++) {
        if(casilla[i]<0 || casilla[i]>7)
            return 1;
    } 
    return 0;
}

// array_append : int** int** int int -> void
// array_append agrega los elementos de un array auxiliar a un array definitivo, tomando el largo del array auxiliar y el del definitivo para no pisar valores.
void array_append(int (*listaDeFichas)[2], int (*listaAuxiliar)[2], int tamanioListaDeFichas, int tamanioListaAuxiliar) {
    int j=tamanioListaDeFichas;
    for(int i=0; i<tamanioListaAuxiliar; i++) {
        listaDeFichas[j][0]=listaAuxiliar[i][0];
        listaDeFichas[j][1]=listaAuxiliar[i][1];
        j++;
    }
}


// hay_jugadas_validas : Tablero* char -> int
// hay_jugadas_validas revisa si el color pasado como argumento puede hacer una jugada en alguna de las casillas almacenadas en el contorno del tablero. Si puede jugar retorna 1, sino 0.
int hay_jugadas_validas(Tablero* tablero, char turno) {
    int tamanioContorno=tablero->cantidadDefichasEnContorno, casilla[2], listaDeFichas[60][2], cantidadFichas;
    for(int i=0; i<tamanioContorno; i++) {
        cantidadFichas=fichas_a_voltear(tablero, tablero->contorno[i], turno, listaDeFichas);
        if(cantidadFichas!=0) {
            return 1;
        }
    }
    return 0;
}

// modificar_tablero : Tablero* char int* int** int -> void
// modificar_tablero realiza las modificaciones necesarias en el tablero y el contorno al colocar una nueva ficha.
void modificar_tablero(Tablero* tablero, char turno, int casilla[], int (*listaDeFichas)[2], int tamanioListaDeFichas) {
    modificar_casillas(tablero, turno, casilla, listaDeFichas, tamanioListaDeFichas);
    modificar_contorno(tablero, casilla);
}

// modificar_casillas : Tablero* char int* int** int -> void
// modificar_casillas coloca la nueva ficha en el tablero y modifica el valor de las casillas cuyas fichas deben cambiar de color.
void modificar_casillas(Tablero* tablero, char turno, int casilla[], int (*listaDeFichas)[2], int tamanioListaDeFichas) {
    tablero->casillas[casilla[0]][casilla[1]] = turno;
    for(int i=0; i<tamanioListaDeFichas; i++) {
        tablero->casillas[listaDeFichas[i][0]][listaDeFichas[i][1]]=turno;
    }
}

// modificar_contorno : Tablero* int* -> void
// modificar_contorno toma el tablero, la nueva casilla ocupada y modifica las casillas contenidas en el contorno.
void modificar_contorno(Tablero* tablero, int casilla[]) {
    int casillasAdyacentes[8][2];
    eliminar_casilla(tablero, casilla);
    int cantidadCasillasAdyacentesVacias = casillas_adyacentes_vacias(tablero, casilla, casillasAdyacentes);
    array_append(tablero->contorno, casillasAdyacentes, tablero->cantidadDefichasEnContorno, cantidadCasillasAdyacentesVacias);
    tablero->cantidadDefichasEnContorno+=cantidadCasillasAdyacentesVacias;
}

// eliminar_casilla : Tablero* int* -> void
// eliminar_casilla toma el tablero y elimina del contorno la casilla pasada como argumento.
void eliminar_casilla(Tablero* tablero, int casilla[]) {
    int casillaEliminada=0;
    for(int i=0; i<(tablero->cantidadDefichasEnContorno)-1; i++) {
        if(casillaEliminada==0 && tablero->contorno[i][0]==casilla[0] && tablero->contorno[i][1]==casilla[1])
            casillaEliminada++;
        if(casillaEliminada==1) {
            tablero->contorno[i][0] = tablero->contorno[i+1][0];
            tablero->contorno[i][1] = tablero->contorno[i+1][1];
        }
    }
    tablero->cantidadDefichasEnContorno-=1;
}

// casillas_adyacentes_vacias : Tablero* int* int** -> int
// casillas_adyacentes_vacias almacena en un array las casillas adycacentes vacías a la nueva casilla ocupada que no están en el contorno y retorna la cantidad de estas.
int casillas_adyacentes_vacias(Tablero* tablero, int casilla[], int (*casillasAdyacentes)[2]) {
    int movimiento[2], i=0, tamanioListaDeFichas=0, cantidadCasillasAdyacentesVacias=0;
    while(i<8) {
        desplazamientos(casilla, i, movimiento);
        if(casilla_fuera_de_rango(movimiento)==0 && tablero->casillas[movimiento[0]][movimiento[1]]=='X' && casilla_en_contorno(tablero, movimiento)==0) {
            casillasAdyacentes[cantidadCasillasAdyacentesVacias][0]=movimiento[0];
            casillasAdyacentes[cantidadCasillasAdyacentesVacias][1]=movimiento[1];
            cantidadCasillasAdyacentesVacias++;
        }
        i++;
    }
    return cantidadCasillasAdyacentesVacias;
}

// casilla_en_contorno : Tablero* int* -> int
// casilla_en_contorno toma el tablero y una casilla y verifica si la casilla está en el contorno. Si lo está retorna 1, sino retorna 0. 
int casilla_en_contorno(Tablero* tablero, int casilla[]) {
    for(int i=0; i<tablero->cantidadDefichasEnContorno; i++) {
        if(tablero->contorno[i][0]==casilla[0] && tablero->contorno[i][1]==casilla[1])
            return 1;
    }
    return 0;
}

// sumar_fichas : Jugador* char int -> void
// sumar_fichas suma al jugador que colocó una ficha en el tablero la ficha que puso y la cantidad de fichas que volteó con su jugada.
void sumar_fichas(Jugador* jugadores, char turno, int fichasASumar) {
    for(int i=0; i<2; i++) {
        if(jugadores[i].color == turno)
            jugadores[i].cantidadDeFichas+=fichasASumar;
        else
            jugadores[i].cantidadDeFichas-=fichasASumar-1;
    }
}

// imprimir_tablero : Tablero* -> void
// imprimir_tablero toma un tablero y lo muestra en pantalla.
void imprimir_tablero(Tablero* tablero) {
    int primeraCasillaFila=0;
    printf("  +--------------------------+\n");
    for(int fila=0; fila<8; fila++) {
        for(int columna=0; columna<8; columna++) {
            if(primeraCasillaFila==0) {
                printf("%d | ", fila+1);
                primeraCasillaFila++;
            }
            printf(" %c ", tablero->casillas[fila][columna]);
        }
        printf(" | \n");
        primeraCasillaFila=0;
    }
    printf("  +--------------------------+\n");
    printf("     A  B  C  D  E  F  G  H\n\n");
}

// partida_finalizada : Tablero* -> int
// partida_finalizada toma el tablero tras haber leido todo el archivo y determina si la partida finalizó (1) o si aún se puede jugar (0).
int partida_finalizada(Tablero* tablero) {
    if(hay_jugadas_validas(tablero, 'B')==1 || hay_jugadas_validas(tablero, 'N')==1)
        return 0;
    return 1;
}

// mostrar_ganador : Jugador* -> void
// mostrar_ganador toma un array de jugadores y muestra quién ganó la partida (o indica que empataron, dado el caso).
void mostrar_ganador(Jugador* jugadores) {
    int fichasJugador0=jugadores[0].cantidadDeFichas, fichasJugador1=jugadores[1].cantidadDeFichas;
    printf("%s (%c): %d fichas\n", jugadores[0].nombre, jugadores[0].color, fichasJugador0);
    printf("%s (%c): %d fichas\n\n", jugadores[1].nombre, jugadores[1].color, fichasJugador1);
    if(fichasJugador0==fichasJugador1)
        printf("Empate!!!\n");
    else if(fichasJugador0 > fichasJugador1)
        printf("El ganador es %s!!!\n", jugadores[0].nombre);
    else
        printf("El ganador es %s!!!\n", jugadores[1].nombre);
}

// volcar_tablero_en_archivo : Tablero FILE* char -> void
// volcar_tablero_en_archivo toma el tablero resultante de una partida incompleta, el color que debe jugar y vuelca la información en un archivo.
void volcar_tablero_en_archivo(Tablero tablero, FILE* tableroFinal) {
    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            fputc((int)tablero.casillas[i][j], tableroFinal);
        }
        fprintf(tableroFinal, "\n");
    }
    fputc((int)tablero.turnoSiguiente, tableroFinal);
}

// liberar_memoria : FILE* FILE* Jugador* -> void
// liberar_memoria libera la memoria pedida con malloc en algún momento del programa.
void liberar_memoria(Jugador* jugadores) {
    free(jugadores[0].nombre);
    free(jugadores[1].nombre);
}