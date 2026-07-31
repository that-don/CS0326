/*
 Il seguente programma presenta una versione corretta, che prende in input un massimo di 10 valori
 ed una versione vulnerabile che prende in input un numero indefinito di valori, riordinando il tutto con un algoritmo bubble sort.
 La versione vulnerabile potrebbe causare un buffer overflow. L'array inizializzato a 10 valori risulta una criticità senza un controllo sull'input.
 tutto questo potrebbe portare alla corruzione di altri dati oppure ad un crash del programma.
 */
#include <stdio.h>

void bubbleSort(int vector[], int n)
{
    int i, j, temp;

    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (vector[j] > vector[j + 1])
            {
                temp = vector[j];
                vector[j] = vector[j + 1];
                vector[j + 1] = temp;
            }
        }
    }
}

void stampa(int vector[], int n)
{
    int i;

    for (i = 0; i < n; i++)
    {
        printf("[%d] %d\n", i + 1, vector[i]);
    }
}

void versioneVulnerabile()
{
    int vector[10];
    int n;
    int i;

    printf("\n=== VERSIONE VULNERABILE ===\n");
    printf("Quanti numeri vuoi inserire? ");
    scanf("%d", &n);

    printf("Inserisci %d numeri:\n", n);

    /* Nessun controllo su n */
    for (i = 0; i < n; i++)
    {
        printf("[%d]: ", i + 1);
        scanf("%d", &vector[i]);
    }

    printf("\nContenuto del vettore:\n");
    stampa(vector, n);

    bubbleSort(vector, n);

    printf("\nVettore ordinato:\n");
    stampa(vector, n);
}

void versioneCorretta()
{
    int vector[10];
    int n;
    int i;

    printf("\n=== VERSIONE SICURA ===\n");

    do
    {
        printf("Quanti numeri vuoi inserire (1-10)? ");
        scanf("%d", &n);

        if (n < 1 || n > 10)
        {
            printf("Errore: il numero deve essere compreso tra 1 e 10.\n");
        }

    } while (n < 1 || n > 10);

    for (i = 0; i < n; i++)
    {
        printf("[%d]: ", i + 1);
        scanf("%d", &vector[i]);
    }

    printf("\nContenuto del vettore:\n");
    stampa(vector, n);

    bubbleSort(vector, n);

    printf("\nVettore ordinato:\n");
    stampa(vector, n);
}

int main()
{
    int scelta;

    do
    {
        printf("\n============================\n");
        printf("1 - Versione vulnerabile\n");
        printf("2 - Versione corretta\n");
        printf("0 - Esci\n");
        printf("============================\n");
        printf("Scelta: ");
        scanf("%d", &scelta);

        switch (scelta)
        {
            case 1:
                versioneVulnerabile();
                break;

            case 2:
                versioneCorretta();
                break;

            case 0:
                printf("Uscita...\n");
                break;

            default:
                printf("Scelta non valida.\n");
        }

    } while (scelta != 0);

    return 0;
}
