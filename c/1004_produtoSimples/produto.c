/**
 * Author: Weder Carlos
 * Date: 30/04/2022
 * To compile: gcc <file_name>.c -o <name_to_execute>
 * To run: ./<name_to_execute>.out
*/

#include <stdio.h>

int main() {
    int num1, num2, prod;
    scanf("%d", &num1);
    scanf("%d", &num2);

    prod = num1 * num2;
    printf("PROD = %d\n", prod);

    return 0;
}