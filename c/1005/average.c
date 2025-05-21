/**
 * Author: Weder Carlos
 * Date: 21/04/2025
 * To compile: gcc <file_name>.c -o <name_to_execute>
 * To run: ./<name_to_execute>.out
*/

#include <stdio.h>

int main() {
    float num1, num2;
    float media;

    scanf("%f", &num1);
    scanf("%f", &num2);

    media = ((num1 * 3.5) + (num2 * 7.5)) / 11;
    printf("MEDIA = %.5f\n", media);

    return 0;
}