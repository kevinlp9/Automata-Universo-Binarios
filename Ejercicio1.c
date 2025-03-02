#include<stdio.h>
#include<stdlib.h>

void generarBinarios(int n, char* resultado, FILE* archivo) {
	int i;
    for (i = 0; i < (1 << n); i++) {
    	int j;
        for (j = 0; j < n; j++) {
            resultado[j] = (i & (1 << (n - 1 - j))) ? '1' : '0';
        }
        resultado[n] = '\0';
        fprintf(archivo, "%s\n", resultado);
        printf("%s,", resultado);
    }
}

int main() {
    int ejecutarDeNuevo = 1;
    while (ejecutarDeNuevo == 1) {
        int n;
        do {
            printf("Ingrese el valor de n (0 <= n <= 1000):\n");
            scanf("%d", &n);
            if (n < 0 || n > 1000) {
                printf("n debe estar en el rango de 0 a 1000.\n\n");
            }
        } while (n < 0 || n > 1000);

        FILE* archivo;
        archivo = fopen("NumeroDigitos.txt", "w");

        printf("E = {e ");
        char resultado[n+1];
        generarBinarios(n, resultado, archivo);

        printf("}");

        fclose(archivo);

        printf("\n\nDatos guardados en 'NumeroDigitos.txt'.\n");
        sleep(1);
        printf("\nDeseas ejecutar nuevamente? (1:SI, 0:NO):\n");
        scanf("%d", &ejecutarDeNuevo);
        getchar();
        sleep(1);
        system("cls");
    }
    return 0;
}

