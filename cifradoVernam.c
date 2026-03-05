#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


// Cifrado de Vernam
// Funciona haciendo XOR para cada caracter del mensaje con un caracter de la clave
// el resultado es el mensaje cifrado
// para descifrarlo se hace el mismo proceso
void cifradoVernam(char *mensaje, char *clave, char *mensaje_cifrado, int len){
    for(int i = 0; i < len; i++){
        mensaje_cifrado[i] = mensaje[i] ^ clave[i]; 
    }

}


// Genera una llave aletoria del mismo tamaño que el mesaje
// la semilla es el tiempo actual
// por tanto es diferente en cada ejecucion del programa
char* generarLlave(int len){

    char *clave = (char*)malloc(len * sizeof(char));
    for(int i = 0; i < len; i++){
        clave[i] = (rand() % 26) + 97; 
    }
    return clave;
}



int main (){
    srand(time(NULL)); 
    char mensaje[150];
    char mensaje_cifrado[150];
    char mensaje_descifrado[150];

    // Recibir mensaje
    printf("Ingrese el mensaje a cifrar: ");
    fgets(mensaje, sizeof(mensaje), stdin);

    // Obtener longitud
    int len = strlen(mensaje);
    char *clave = generarLlave(len);
    printf("Clave generada: %s\n", clave);

    cifradoVernam(mensaje, clave, mensaje_cifrado, len);
    printf("Mensaje cifrado: %s\n", mensaje_cifrado);
    cifradoVernam(mensaje_cifrado, clave, mensaje_descifrado, len);
    printf("Mensaje descifrado: %s\n", mensaje_descifrado);

}