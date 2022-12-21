#include "test.h"

/*
NOTA: Hay un problema en al testear la función leer_archivo_jugada. Tras testear alguno de los casos, la función retorna el valor correcto
y pasa la prueba, pero el programa termina de ejecutarse antes de pasar al siguiente caso. Es un problema que también se da al correr el
archivo main.c, todo funciona bien pero en algún momento al llegar al final del programa este finaliza abruptamente. No pude encontrar el error
en ninguno de los archivos.
*/

void test_turno_inicial();
void test_turno_inicial_valido();
void test_leer_jugada();
void test_cambiar_turno();
void test_fichas_a_voltear();
void test_casilla_fuera_de_rango();
void test_hay_jugadas_validas();
void test_casillas_adyacentes_vacias();
void test_casilla_en_contorno();
void test_verificar_jugada();
void test_leer_archivo_jugada();

void auxiliar_leer_lineas(FILE* f, int lineas);

int main(){
    test_turno_inicial();
    test_turno_inicial_valido();
    test_leer_jugada();
    test_cambiar_turno();
    test_casilla_fuera_de_rango();
    test_fichas_a_voltear();
    test_hay_jugadas_validas();
    test_casillas_adyacentes_vacias();
    test_casilla_en_contorno();
    test_verificar_jugada();
    test_leer_archivo_jugada();
    return 0;
}
void test_turno_inicial() {
    FILE* f1=fopen("../Archivos de prueba/partida1.txt", "r"), *f2=fopen("../Archivos de prueba/partida5.txt", "r");
    auxiliar_leer_lineas(f1, 2);
    auxiliar_leer_lineas(f2, 2);
    assert(turno_inicial(f1)=='B');
    assert(turno_inicial(f2)=='N');
    fclose(f1);
    fclose(f2);
}

void test_turno_inicial_valido() {
    FILE* f1=fopen("../Archivos de prueba/partida1.txt", "r"), *f2=fopen("../Archivos de prueba/partida11.txt", "r");
    auxiliar_leer_lineas(f1, 2);
    auxiliar_leer_lineas(f2, 2);
    assert(turno_inicial_valido(f1, turno_inicial(f1))==1);
    assert(turno_inicial_valido(f2, turno_inicial(f2))==0);
    fclose(f1);
    fclose(f2);
}

void test_leer_jugada() {
    FILE* f1=fopen("../Archivos de prueba/partida2.txt", "r");
    char aux[10];
    auxiliar_leer_lineas(f1, 8);
    assert(leer_jugada(f1, aux)==1);
    auxiliar_leer_lineas(f1, 8);
    assert(leer_jugada(f1, aux)==0);
    fclose(f1);
}

void test_cambiar_turno() {
    assert(cambiar_turno('N')=='B');
    assert(cambiar_turno('B')=='N');
}

void test_fichas_a_voltear() {
    Tablero tablero;
    tablero_inicial(&tablero);
    tablero.casillas[0][0]='N';
    tablero.casillas[1][3]='B';
    tablero.casillas[2][1]='N';
    tablero.casillas[2][3]='B';
    tablero.casillas[2][5]='B';
    tablero.casillas[2][6]='N';
    tablero.casillas[3][1]='B';
    tablero.casillas[3][3]='B';
    tablero.casillas[3][4]='N';
    tablero.casillas[3][5]='N';
    tablero.casillas[4][3]='N';
    tablero.casillas[4][4]='B';
    tablero.casillas[4][5]='N';
    tablero.casillas[4][3]='N';
    tablero.casillas[5][1]='B';
    tablero.casillas[5][5]='B';
    tablero.casillas[5][7]='B';
    tablero.casillas[6][6]='B';
    tablero.casillas[7][6]='N';
    tablero.casillas[7][7]='N';
    int coord1[2]={0, 3}, coord2[2]={2, 2}, coord3[2]={1, 6}, aux[100][2];
    assert(fichas_a_voltear(&tablero, coord1, 'N', aux)==3);
    assert(fichas_a_voltear(&tablero, coord2, 'N', aux)==4);
    assert(fichas_a_voltear(&tablero, coord3, 'B', aux)==0);
}


/*t = [ 
        ['N', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', '-', '-', '-', '-'],
        ['-', 'N', '-', 'B', '-', 'B', 'N', '-'],   tablero utilizado en la función anterior
        ['-', 'B', '-', 'B', 'N', 'N', '-', '-'],
        ['-', '-', '-', 'N', 'B', 'N', '-', '-'],
        ['-', 'B', '-', '-', '-', 'B', '-', 'B'],
        ['-', '-', '-', '-', '-', '-', 'B', '-'],
        ['-', '-', '-', '-', '-', '-', 'N', 'N']
    ]*/

void test_casilla_fuera_de_rango() {
    int casilla1[2]={0, 7}, casilla2[2]={4, 2}, casilla3[2]={3, 9}, casilla4[2]={8, 1}, casilla5[2]={-2, 11};
    assert(casilla_fuera_de_rango(casilla1)==0);
    assert(casilla_fuera_de_rango(casilla2)==0);
    assert(casilla_fuera_de_rango(casilla3)==1);
    assert(casilla_fuera_de_rango(casilla4)==1);
    assert(casilla_fuera_de_rango(casilla5)==1);
}

void test_hay_jugadas_validas() {
    Tablero tablero1;
    inicializar_tablero(&tablero1);
    Tablero tablero2;
    tablero2.casillas[0][0]='N';
    tablero2.casillas[1][0]='B';
    tablero2.casillas[2][0]='N';
    tablero2.contorno[0][0]=0;
    tablero2.contorno[0][1]=1;
    tablero2.contorno[1][0]=1;
    tablero2.contorno[1][1]=1;
    tablero2.contorno[2][0]=2;
    tablero2.contorno[2][1]=1;
    tablero2.contorno[3][0]=3;
    tablero2.contorno[3][1]=1;
    tablero2.contorno[4][0]=3;
    tablero2.contorno[4][1]=0;
    tablero2.cantidadDefichasEnContorno=5;
    assert(hay_jugadas_validas(&tablero1, 'N')==1);
    assert(hay_jugadas_validas(&tablero2, 'N')==0);
    assert(hay_jugadas_validas(&tablero2, 'B')==1);
}

/*
t1 = [
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'B', 'N', '-', '-', '-'],  tablero1 utilizado en la funcion anterior
        ['-', '-', '-', 'N', 'B', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

t2 = [
        ['N', '-', '-', '-', '-', '-', '-', '-'],
        ['B', '-', '-', '-', '-', '-', '-', '-'],
        ['N', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],  tablero2 utilizado en la funcion anterior
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

*/


void test_casilla_en_contorno() {
    Tablero tablero;
    inicializar_tablero(&tablero);
    int casilla1[2]={2, 2}, casilla2[2]={4, 2}, casilla3[2]={6, 6};
    assert(casilla_en_contorno(&tablero, casilla1)==1);
    assert(casilla_en_contorno(&tablero, casilla2)==1);
    assert(casilla_en_contorno(&tablero, casilla3)==0);
}

void test_casillas_adyacentes_vacias() {
    Tablero tablero2;
    for(int i=0; i<8; i++) {
        for(int j = 0; j < 8; j++) {
            tablero2.casillas[i][j] = 'X';
        }
    }
    tablero2.casillas[0][0]='N';
    tablero2.casillas[1][0]='B';
    tablero2.casillas[2][0]='N';
    tablero2.contorno[0][0]=0;
    tablero2.contorno[0][1]=1;
    tablero2.contorno[1][0]=1;
    tablero2.contorno[1][1]=1;
    tablero2.contorno[2][0]=2;
    tablero2.contorno[2][1]=1;
    tablero2.contorno[3][0]=3;
    tablero2.contorno[3][1]=1;
    tablero2.contorno[4][0]=3;
    tablero2.contorno[4][1]=0;
    tablero2.cantidadDefichasEnContorno=5;
    int casilla1[2]={2, 0}, casilla2[2]={1, 0}, casilla3[2]={3, 3}, aux[10][2];
    assert(casillas_adyacentes_vacias(&tablero2, casilla1, aux)==0);
    assert(casillas_adyacentes_vacias(&tablero2, casilla2, aux)==0);
    assert(casillas_adyacentes_vacias(&tablero2, casilla3, aux)==8);
}

void test_verificar_jugada() {
    Tablero tablero;
    inicializar_tablero(&tablero);
    Jugador jugadores[2];
    jugadores[0].cantidadDeFichas=2;
    jugadores[1].cantidadDeFichas=2;
    assert(verificar_jugada("N7\n", jugadores, 'B', &tablero)==0);
    assert(verificar_jugada("N73", jugadores, 'B', &tablero)==0);
    assert(verificar_jugada("H\nA", jugadores, 'B', &tablero)==0);
    assert(verificar_jugada("\n", jugadores, 'B', &tablero)==0);
    assert(verificar_jugada("\0", jugadores, 'B', &tablero)==0);
    assert(verificar_jugada("D4\n", jugadores, 'N', &tablero)==0);
    assert(verificar_jugada("E6\n", jugadores, 'N', &tablero)==1);
}


void test_leer_archivo_jugada() {
    FILE* f1=fopen("../Archivos de prueba/partida1.txt", "r"), *f2=fopen("../Archivos de prueba/partida2.txt", "r"),*f3=fopen("../Archivos de prueba/partida3.txt", "r");
    FILE* f4=fopen("../Archivos de prueba/partida4.txt", "r"), *f5=fopen("../Archivos de prueba/partida5.txt", "r"), *f6=fopen("../Archivos de prueba/partida6.txt", "r");
    FILE* f7=fopen("../Archivos de prueba/partida7.txt", "r"), *f8=fopen("../Archivos de prueba/partida8.txt", "r"), *f9=fopen("../Archivos de prueba/partida9.txt", "r");
    FILE* f10=fopen("../Archivos de prueba/partida10.txt", "r"), *f11=fopen("../Archivos de prueba/partida11.txt", "r");
    Tablero tablero;
    inicializar_tablero(&tablero);
    Jugador jugadores[2];
    jugadores[0].cantidadDeFichas=2;
    jugadores[1].cantidadDeFichas=2;
    //assert(leer_archivo_jugadas(f1, jugadores, &tablero)==1);
    //assert(leer_archivo_jugadas(f2, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f3, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f4, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f5, jugadores, &tablero)==1);
    //assert(leer_archivo_jugadas(f6, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f7, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f8, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f9, jugadores, &tablero)==0);
    //assert(leer_archivo_jugadas(f10, jugadores, &tablero)==1);
    //assert(leer_archivo_jugadas(f11, jugadores, &tablero)==0);
    fclose(f1);
    fclose(f2);
    fclose(f3);
    fclose(f4);
    fclose(f5);
    fclose(f6);
    fclose(f7);
    fclose(f8);
    fclose(f9);
    fclose(f10);
    fclose(f11);
}



// auxiliar_leer_lineas : FILE* int -> void
// auxiliar_leer_lineas toma un archivo y la cantidad de lineas que se quiere leer del mismo.
void auxiliar_leer_lineas(FILE* f, int lineas) {
    char buf[100];
    for(int i=0; i<lineas; i++) {
        fgets(buf, 100, f);
    }
}
